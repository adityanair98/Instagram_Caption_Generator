import streamlit as st  
from PIL import Image, ImageOps
import numpy as np

## use $ streamlit run app.py to run app!


# hide deprication warnings
import warnings
warnings.filterwarnings("ignore")

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
        st.subheader("Welcome to InstaMuse, the ultimate tool for turning your snapshots into social media sensations!")
        st.write("Start turning heads with your posts. Use InstaMuse now and watch your likes soar! ")

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

## For Bhumika!!! 
# Modeling part
file = st.file_uploader("", type=["jpg", "png"])
def import_and_predict(image_data):  # Will also need to import model I think? 
        size = (224,224)
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        img = np.asarray(image)
        img_reshape = img[np.newaxis,...]
        # Prediction is model output
        prediction = "Happy Days! #gradlife" # Place holder for now, model.predict(img_reshape)? 
        return prediction


if file is None:
    st.text("Upload your photo now and let the caption fun begin!")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    # Predictions should be the output captins
    predictions = import_and_predict(image)  # Alter to whatever arguments the model takes
    st.markdown("## Captions:")
    st.info(predictions)
