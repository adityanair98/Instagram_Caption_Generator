"""
This script contains the CaptionGenerator class,
which is used to generate Instagram captions for images
using BLIP and Gemini models.
"""
import google.generativeai as genai
import streamlit as st
import app_utils as utils

genai.configure(api_key=utils.get_gemini_api_key())


class CaptionGenerator:
    """
    Class for generating Instagram captions for images using BLIP and Gemini models.
    The model from Hugging Face is used to generate the initial caption for the image,
    which is then used as a prompt for the Gemini model to generate five distinct and
    engaging captions for the image.

    Attributes:
    - gemini: GenerativeModel - The Gemini model used to generate Instagram captions.
    - processor: AutoProcessor - The processor used to prepare the image for caption generation.
    - model: Blip2ForConditionalGeneration - The BLIP-2 model used to generate the initial caption.
    Methods:
    - image_2_text(image_data): Generate a caption for the provided image using the BLIP-2 model.
    - text_2_caption(image_description): Generate five Instagram captions for the provided image.
    - caption_2_hashtag(caption): Generate additional hashtags based on the content of the caption.
    """
    def __init__(self):
        self.gemini = genai.GenerativeModel('gemini-pro')
        self.processor = None
        self.model = None

    def image_2_text(self, image_data, processor, model):
        """
        Generate a caption for the provided image using the BLIP-2 model.
        :param image_data: PIL.Image - The image for which a caption
        is to be generated.
        :param processor: AutoProcessor - The processor used to prepare the
        image for caption generation.
        :param model: Blip2ForConditionalGeneration - The BLIP-2 model used
        :return: description - The description generated for the image.
        """
        try:
            inputs = processor(images=image_data, return_tensors="pt")
            generated_ids = model.generate(**inputs, max_length=100)
            description = processor.batch_decode(generated_ids, skip_special_tokens=True)[0].strip()
            return description

        except Exception as e:
            st.error(f"Error occurred during image captioning: {e}")

    def text_2_caption(self, image_description):
        """
        Generate five Instagram captions for the provided BLIP-2 image description
        using the Gemini model.
        :param image_description: str - The description generated for the image.
        :return: caption - The caption generated for the image.
        :return: caption_list - A list of five distinct and engaging captions for the image.
        :return: image_description - The description generated for the image.
        """
        prompt = (
            f"This caption was generated with a deep learning model."
            f"Your task is to enhance the caption to make it more engaging:"
            f"Given this provided photo description, generate five distinct "
            f"fun and engaging Instagram captions. Each caption must include "
            f"at least one emoji and one hashtag. The captions should be "
            f"formatted with a preceding 'Caption #', followed by the "
            f"caption text. Ensure each caption is separated by a blank "
            f"line for readability."
            f"Original Caption: {image_description}"
            f"Please format your response as follows: \n"
            f"**Caption 1**: [caption text]\n"
            f"**Caption 2**: [caption text]\n"
            f"**Caption 3**: [caption text]\n"
            f"**Caption 4**: [caption text]\n"
            f"**Caption 5**: [caption text]\n"
        )

        try:
            response = self.gemini.generate_content(prompt)
            caption = response.parts[0].text
            caption_list = response.parts[0].text.split("\n")
            return caption, caption_list, image_description

        except Exception as e:
            st.error(f"Unable to connect to Gemini API: {e}")

    def caption_2_hashtag(self, caption):
        """
        Generate additional hashtags based on the content of the caption.
        :param: caption - The caption generated for the image.
        :return: hashtags - The hashtags generated based on the content of the caption.
        """
        # Generate hashtags based on the content of the caption
        prompt = (
            f"Given the provided caption, generate relevant hashtags to increase engagement,"
              f"and are related to the caption content. Original Image Description: {caption},"
              f"Please format your response as follows:\n"
              f'[hashtags separated by commas]'
              f" \n"
        )

        try:
            response = self.gemini.generate_content(prompt)
            hashtags = response.parts[0].text
            return hashtags

        except Exception as e:
            st.error(f"Error occurred with Gemini API: {e}")


# Example usage of the CaptionGenerator class
# caption_generator = load_model()
# image = Image.open("example.jpg")
# desc = caption_generator.image_2_text(image)
# captions, caption_list, img_description = caption_generator.text_2_caption(desc)
# hashtags = caption_generator.caption_2_hashtag(img_description)
# print(captions)
# print(hashtags)
