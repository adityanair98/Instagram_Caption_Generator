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
         ### Drag your photo here and spark some caption magic! ✨
         """)

# Upload image file and process image
file = st.file_uploader("Upload your image here:", type=["jpg", "png"])

if file is not None:
    col1, col2 = st.columns(2)
    with col1:
        try:
            st.write("#### 📸 **Image**:")
            image = Image.open(file).convert('RGB')
            image.thumbnail((400, 400))
            st.image(image, caption='Uploaded Image')

        except Exception as e:
            st.error(f"Error loading image: {e}")

    with col2:
        # Add space before the spinner to center it
        space_above = st.empty()
        space_above.markdown("<br>" * 5, unsafe_allow_html=True)

        # Create spinner while captions are generating
        with st.spinner('Generating captions... Please wait'):
            try:
                caption_generator = script.InstagramCaptionGenerator()
                response = caption_generator.predict(image)
                captions = response
            except ValueError as e:
                st.error(f"Error obtaining captions: {e}")
            except Exception as e:
                st.error(f"Error generating caption: {e}")
                captions = None
        
        # Clear space
        space_above.empty()

        # Display captions
        if captions:
            st.write("#### 📝 **Generated Captions**:")
            st.write(response)
        else:
            st.text("Please upload an image to generate captions.")
