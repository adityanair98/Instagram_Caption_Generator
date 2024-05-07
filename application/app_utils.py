"""
Utility functions for the Instagram Caption Generator app.
"""
import os
from pathlib import Path

from dotenv import load_dotenv
import pandas as pd
import streamlit as st
from transformers import AutoProcessor, Blip2ForConditionalGeneration


def get_gemini_api_key():
    """
    Retrieves the Google API key from the environment variables,
    which is used to configure the Gemini model.
    :return: str - The Google API key.
    """
    load_dotenv()
    google_api_key = os.getenv("GOOGLE_API_KEY")
    return google_api_key


@st.cache_resource()
def init_model():
    """
    Initializes the BLIP-2 model and processor for image captioning.
    The cache_resource decorator is used to cache the model and processor.
    The streamlit app can call this function to load the model and processor
    without reinitializing it.
    :return: AutoProcessor - The processor used to prepare the image for caption generation.
    :return: Blip2ForConditionalGeneration - The BLIP-2 model used to generate the initial caption.
    """
    try:
        processor = AutoProcessor.from_pretrained(
            os.path.expanduser('~/data/pretrained/blip2-opt-2.7b')
        )
        blip2_model = Blip2ForConditionalGeneration.from_pretrained(
            os.path.expanduser('~/data/pretrained/blip2-opt-2.7b')
        )
        return processor, blip2_model
    except Exception as e:
        st.error(f"Error occurred during model initialization: {e}")


# Function to store the user data to a CSV file
def save_user_data(first_name, last_name, email, phone):
    """
    Function to store the user data to a CSV file

    :param first_name: str - First name of the user
    :param last_name: str - Last name of the user
    :param email: str - Email of the user
    :param phone: str - Phone number of the user
    :return: None
    """
    csv_file = Path("./user_data/user_data.csv")
    # Check if the file exists and create a DataFrame accordingly
    if csv_file.exists():
        df = pd.read_csv(csv_file)
    else:
        df = pd.DataFrame(
            columns=["First Name", "Last Name", "Email", "Phone Number"]
        )
    new_data = {
        "First Name": first_name,
        "Last Name": last_name,
        "Email": email,
        "Phone Number": phone
    }
    df = df.append(new_data, ignore_index=True)
    df.to_csv(csv_file, index=False)
    return None


def get_gif(path):
    """
    Function to get the GIF image from the specified path.
    :param path: str - Path to the GIF image
    :return: bytes - The GIF image
    """
    with open(path, "rb") as file:
        gif = file.read()
    return gif


# Blip-2 does most of the standard image processing needed for image captioning.
def process_image():
    """
    Unused function for image processing,
    not needed for the current implementation.
    """
    pass
