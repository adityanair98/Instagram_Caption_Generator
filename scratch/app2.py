"""
This script defines the InstaMuse app, which generates Instagram captions for
uploaded images. The app uses two models: BLIP for image captioning and Gemini
for generating Instagram captions. The app is built using Streamlit and the
Google Generative AI API, along with the Hugging Face Transformers library.
"""

from os import getenv
import streamlit as st
from PIL import Image
from torchvision import transforms
from transformers import AutoProcessor, BlipForConditionalGeneration
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = getenv("GOOGLE_API_KEY")

# Configure the generative AI API
genai.configure(api_key=GOOGLE_API_KEY)
gemini_model = genai.GenerativeModel('gemini-pro')

# Initialize the models
blip_processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def import_and_predict(image_data):
    """
    Creates five possible Instagram captions for an image.

    Args:
    - image_data: Image data in RGB format.

    Returns:
    - response.text: The five Instagram captions in text format.
    """
    transform = transforms.Compose([
        transforms.Resize((1080, 1080))
    ])
    uploaded_image = transform(image_data)

    # BLIP Description Generation
    inputs = blip_processor(images=uploaded_image, return_tensors="pt")
    generated_ids = blip_model.generate(
        **inputs,
        max_new_tokens=100,
        max_length=100
    )
    caption = blip_processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

    # Gemini Caption Generation
    prompt = (
        f"Given the provided photo caption, generate five distinct "
        f"and engaging Instagram captions. Each caption must include "
        f"at least one emoji and one hashtag. The captions should be "
        f"formatted with a preceding 'Caption #', followed by the "
        f"caption text. Ensure each caption is separated by a blank "
        f"line for readability.\n\n"
        f"Original Caption: {caption}\n\n"
        f"Please format your response as follows:\n"
        f"**Caption 1**: [caption text] \n"
        f"**Caption 2**: [caption text] \n"
        f"**Caption 3**: [caption text] \n"
        f"**Caption 4**: [caption text] \n"
        f"**Caption 5**: [caption text] \n"
    )
    response = gemini_model.generate_content(prompt)
    return response.parts[0].text


# Define Streamlit configurations
st.set_page_config(page_title="Instamuse", page_icon=":camera:", initial_sidebar_state='auto')

# Sidebar configuration
with st.sidebar:
    st.image('insta.png')
    st.title("InstaMuse")
    st.subheader("Welcome to InstaMuse, the ultimate tool for turning your snapshots into social media sensations!")
    st.write("Start turning heads with your posts. Use InstaMuse now and watch your likes soar!")

# Main page content
st.write("""
         # InstaMuse 🌟📸

         Struggling to find the perfect words to match your pictures? Let InstaMuse do the heavy lifting! 
         With just a simple upload, our app uses cutting-edge technology to analyze your image and generate a 
         witty, engaging, or inspiring caption that captures the essence of your moment.

         Whether you’re a selfie savant, a nature explorer, or a foodie fanatic, InstaMuse is here to amplify 
         your Instagram presence. Jazz up your feed with tailored captions that resonate with your followers and 
         attract new eyes to your profile. It’s quick, easy, and fun!

         **Drag your photo here and spark some caption magic!** ✨
         """)

# Upload image file and process image
file = st.file_uploader("Upload your image here:", type=["jpg", "png"])

if file is not None:
    col1, col2 = st.columns(2)
    with col1:
        image = Image.open(file).convert('RGB')
        image.thumbnail((400, 400))
        st.image(image, caption='Uploaded Image')

    with col2:
        predictions = import_and_predict(image)
        st.markdown("#### Captions:")
        st.write(predictions)
else:
    st.text("Please upload an image to generate captions.")
