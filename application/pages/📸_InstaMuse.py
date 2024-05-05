import os
import streamlit as st
from PIL import Image
import pyperclip
import app_utils as utils
from CaptionGenerator import CaptionGenerator, load_model

# Define Streamlit configurations
st.set_page_config(
    page_title="Instamuse", 
    page_icon=":camera:", 
    layout='wide', 
    menu_items={
        'Get Help': 'https://www.streamlit.io',
        'Report a bug': "https://github.com/aditya-67/Instagram_Caption_Generator/issues",
        'About': "# This is a Streamlit app that uses AI to generate captions for images."
    }
)

# Initialize the caption generator
caption_generator = load_model()

# Define aesthetic enhancements, including CSS for the spinner
st.markdown(
    """
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .image-shadow {
        box-shadow: 8px 8px 20px grey;
    }
    /* Centering the spinner */
    .st-bq {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        font-size: 20px;  /* Make text larger */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar configuration
with st.sidebar:
    st.image(os.path.join('images', 'insta.png'), width=300)
    st.title("Welcome to InstaMuse!")
    st.subheader("Turn your snapshots into social media sensations.")
    st.write("Start turning heads with your posts. Use InstaMuse now and watch your likes soar!")

# Main page content
st.markdown('<p class="big-font">InstaMuse Photo Caption Generator</p>', unsafe_allow_html=True)
st.write("### Upload your photo below and spark some caption magic! ଘ(੭ˊᵕˋ)੭* ੈ✩‧₊")

# Upload image file and process image
file = st.file_uploader(
    "Upload your image here:",
    type=["jpg", "png"],
    help="Only jpg and png images are supported"
)

if file:
    image = Image.open(file)
    image.thumbnail((600, 600), Image.Resampling.LANCZOS)

    try:
        desc = caption_generator.image_2_text(image)
        captions, caption_list, img_description = caption_generator.text_2_caption(desc)
        st.session_state['captions'] = captions
        st.session_state['caption_list'] = caption_list
        st.session_state['img_description'] = img_description
    except Exception as e:
        st.error(f"Error generating captions: {e}")
        captions = None

    with st.spinner(r'#### :sparkles: :sparkles: Generating... please wait :hourglass_flowing_sand:'):
        st.session_state['file'] = file

        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.markdown("## 📸 Your Image:")
                st.image(image, caption='Uploaded Image', use_column_width=True)

            with col2:
                if captions:
                    st.markdown("## 📝 Generated Captions:")
                    for caption in caption_list:
                        if caption.strip():
                            st.info(f"##### {caption}")

    # Action buttons with functionality
    if 'captions' in st.session_state and st.session_state['captions']:
        col1, col2, col3, col4 = st.columns(4)
        if col1.button("📋 Copy"):
            pyperclip.copy(st.session_state['captions'])
            st.success("Caption copied to clipboard!")

        if col2.button("🔄 Regenerate"):
            with st.spinner('Regenerating captions...'):
                st.rerun()

        if col3.button("✨ More Hashtags"):
            with st.spinner('Generating hashtags...'):
                try:
                    hashtags = caption_generator.caption_2_hashtag(st.session_state['img_description'])
                except Exception as e:
                    st.error(f"Error generating hashtags: {e}")
                    hashtags = None
                st.write("### Generated Hashtags:")
                st.write(f"**{hashtags}**")

        if col4.button(":window: Clear Screen"):
            st.rerun()

with st.expander("Need help?"):
    st.write("Please contact us at [email](mailto:jess@llmjessica.com)")

# Footer
st.markdown("---")
st.caption("Thank you for using InstaMuse! Feel free to contact us for any suggestions or issues.")
