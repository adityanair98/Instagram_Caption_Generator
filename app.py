import streamlit as st
from PIL import Image, ImageOps
import numpy as np
import pickle
from torchvision import transforms


# use $ streamlit run app.py to run app!

# hide deprication warnings
import warnings
warnings.filterwarnings("ignore")

# BLIP Model
from transformers import BlipForConditionalGeneration, BlipProcessor
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Caption Model
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
caption_tokenizer = AutoTokenizer.from_pretrained("prasanthsagirala/text-to-social-media-captions")
caption_model = AutoModelForSeq2SeqLM.from_pretrained("prasanthsagirala/text-to-social-media-captions")

# with open("models/blip_model.pkl", "rb") as f:
#     blip_model = pickle.load(f)

# with open("models/caption_tokenizer.pkl", "rb") as f:
#     caption_tokenizer = pickle.load(f)

# with open("models/caption_model.pkl", "rb") as f:
#     caption_model = pickle.load(f)


# Set pre-defined page configurations
st.set_page_config(
    page_title="Instamuse",  # Title
    page_icon=":camera:",  # log-icon
    initial_sidebar_state='auto'  # page loading state
)

# Sidebard (left side of page)
with st.sidebar:
    st.image('insta.png')
    st.title("InstaMuse")
    st.subheader(
        "Welcome to InstaMuse, the ultimate tool for turning your snapshots into social media sensations!")
    st.write(
        "Start turning heads with your posts. Use InstaMuse now and watch your likes soar! ")

# Main page text
st.write("""
         # InstaMuse  🌟📸

        Struggling to find the perfect words to match your pictures? Let InstaMuse do the heavy \
        lifting! With just a simple upload, our app uses cutting-edge technology to analyze your \
        image and generate a witty, engaging, or inspiring caption that captures the essence of \
        your moment. \n \

        Whether you’re a selfie savant, a nature explorer, or a foodie fanatic, InstaMuse is here to \
        amplify your Instagram presence. Jazz up your feed with tailored captions that resonate with your \
        followers and attract new eyes to your profile. It’s quick, easy, and fun!

        **Drag your photo here and spark some caption magic!** ✨
         """
         )

# For Bhumika!!!
# Modeling part
file = st.file_uploader("", type=["jpg", "png"])


def import_and_predict(image_data):  # Will also need to import model I think?
    transform = transforms.Compose([
        transforms.Resize((1080, 1080))
    ])
    image = transform(image_data)

    # BLIP Description Generation
    inputs = blip_processor(images=image, return_tensors="pt")
    generated_ids = blip_model.generate(**inputs, max_new_tokens=50)
    generated_text = blip_processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()

    # Caption Generation
    inputs = ["Instagram captionize:" + generated_text]
    inputs = caption_tokenizer(inputs, max_length=512, truncation=True, return_tensors="pt")
    output = caption_model.generate(**inputs, num_beams=8, do_sample=True, min_length=10, max_length=64)
    decoded_output = caption_tokenizer.batch_decode(output, skip_special_tokens=True)[0]
    return decoded_output


if file is None:
    st.text("Upload your photo now and let the caption fun begin!")
else:
    image = Image.open(file).convert('RGB')
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image)
    st.markdown("## Captions:")
    st.info(predictions)
