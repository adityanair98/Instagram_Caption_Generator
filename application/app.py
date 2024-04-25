"""
This script defines the InstaMuse app, which generates Instagram captions for
uploaded images. The app uses two models: BLIP for image captioning and Gemini
for generating Instagram captions. The app is built using Streamlit and the
Google Generative AI API, along with the Hugging Face Transformers library.
"""
import streamlit as st
from PIL import Image
import script

# Define Streamlit configurations
st.set_page_config(page_title="Instamuse", page_icon=":camera:", initial_sidebar_state='auto')

# Sidebar configuration
with st.sidebar:
    st.image('insta.png')
    st.title("InstaMuse")
    st.subheader("Welcome to InstaMuse, the ultimate tool for turning\
     your snapshots into social media sensations!")
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
        try:
            image = Image.open(file).convert('RGB')
            image.thumbnail((400, 400))
            st.image(image, caption='Uploaded Image')

        except Exception as e:
            st.error(f"Error loading image: {e}")

    with col2:
        try:
            st.write("### Generating Captions... 🧠")
            caption_generator = script.InstagramCaptionGenerator()
            response = caption_generator.import_and_predict(image)
            captions = response
            st.write("### 📝 **Generated Captions**:")
            st.write(response)

        except ValueError as e:
            st.error(f"Error obtaining captions: {e}")

        except Exception as e:
            st.error(f"An unknown error occurred"
                     f"Error Message: {e}")

else:
    st.text("Please upload an image to generate captions.")
