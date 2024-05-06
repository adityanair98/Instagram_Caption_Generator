import os
import streamlit as st
from PIL import Image
import pyperclip
import CaptionGenerator
import app_utils as utils

# Define Streamlit configurations
st.set_page_config(page_title="Instamuse", page_icon=":camera:", layout='wide')

# Initialize the caption generator
caption_generator = CaptionGenerator.CaptionGenerator()


# Sidebar configuration
with st.sidebar:
    st.image(os.path.join('images', 'insta.png'), width=300)
    st.title("Welcome to InstaMuse!")
    st.subheader("Turn your snapshots into social media sensations.")
    st.write("Start turning heads with your posts. Use InstaMuse now and watch your likes soar!")

# Main page content
st.markdown('<p class="big-font">InstaMuse Photo Caption Generator</p>', unsafe_allow_html=True)
st.write("""### Upload your photo below and spark some caption magic! ଘ(੭ˊᵕˋ)੭* ੈ✩‧₊""")

# Load the model for image description
with st.spinner('Loading Application, this make take a minute :hourglass_flowing_sand:'):
    # Load the model for image captioning
    model, processor = utils.init_model()

# Upload image file and process image
uploaded_file = st.file_uploader(
    "Upload your image here:", type=["jpg", "png"], help="Only jpg and png images are supported"
)


if uploaded_file is not None:
    if 'file' not in st.session_state or uploaded_file != st.session_state['file']:
        st.session_state['file'] = uploaded_file

    image = Image.open(st.session_state['file'])
    image.thumbnail((400, 400), Image.Resampling.LANCZOS)
    st.session_state['image'] = image
    col1, col2 = st.columns(2)

    with st.container():
        with col1:
            st.markdown("## 📸 Your Image:")
            st.image(st.session_state['image'], caption='Uploaded Image', use_column_width=True)

        with col2:
            with st.spinner(r'#### :sparkles: :sparkles: Generating... please wait :hourglass_flowing_sand:'):
                if 'captions' not in st.session_state:
                    desc = caption_generator.image_2_text(image, model, processor)
                    captions, caption_list, img_description = caption_generator.text_2_caption(desc)
                    st.session_state['captions'] = captions
                    st.session_state['caption_list'] = caption_list
                    st.session_state['img_description'] = img_description
                    st.empty()
                    st.markdown("## 📝 Generated Captions:")
                    for caption in st.session_state['caption_list']:
                        if caption.strip() != "":
                            st.info(f"##### {caption}")

                else:
                    st.markdown("## 📝 Generated Captions:")
                    for caption in st.session_state['caption_list']:
                        if caption.strip() != "":
                            st.info(f"##### {caption}")

        st.markdown("---")

        col3, col4, col5, col6 = st.columns(4)
        if col3.button("📋 Copy Captions"):
            pyperclip.copy(st.session_state['captions'])
            st.success("Captions copied to clipboard!")

        if col4.button("🔄 Regenerate Captions"):
            # Forcefully clear file to trigger reprocessing
            if 'file' in st.session_state:
                del st.session_state['file']
                del st.session_state['captions']
                del st.session_state['caption_list']
                del st.session_state['img_description']
                st.rerun()

        if col5.button("✨ More Hashtags"):
            if 'img_description' in st.session_state:
                with st.spinner('Generating hashtags...'):
                    try:
                        hashtags = caption_generator.caption_2_hashtag(st.session_state['img_description'])
                        st.write("### Generated Hashtags:")
                        st.write(f"**{hashtags}**")
                    except Exception as e:
                        st.error(f"Error generating hashtags: {e}")

        if col6.button(":x: Report Issue"):
            st.write("You are beta testing this app. Please report any issues to the developer. Thank you")


st.markdown("---")

with st.expander("Need help?"):
    st.write("Please contact us by [email](mailto:jess@llmjessica.com)")  # Correct the email link

st.markdown("---")

st.caption("Thank you for using InstaMuse! Feel free to contact us for any suggestions or issues.")
