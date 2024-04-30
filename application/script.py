"""
This script defines the InstagramCaptionGenerator class, which generates Instagram captions
for images using the Google Generative AI API and the Hugging Face Transformers library
(BLIP and Gemini models). The model from Hugging Face is used to generate the initial
caption for the image, which is then used as a prompt for the Gemini model to generate
five distinct and engaging captions for the image.
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai
from transformers import AutoProcessor, BlipForConditionalGeneration
from torchvision import transforms


class InstagramCaptionGenerator:
    """
    Class for generating Instagram captions for images using BLIP and Gemini models.

    Attributes:
    - google_api_key (str): Google API key for accessing the Generative AI API.
    - gemini_model (GenerativeModel): Gemini model for generating Instagram captions.
    - blip_processor (AutoProcessor): BLIP model processor for image captioning.
    - blip_model (BlipForConditionalGeneration): BLIP model for image captioning.

    Methods:
    - process_image(image_data): Resize and prepare the image for caption generation.
    - predict(image_data): Generate five Instagram captions for the provided image.
    """
    def __init__(self):
        # Load environment variables
        #load_dotenv()
        #self.google_api_key = os.getenv("GOOGLE_API_KEY")
        genai.configure(api_key='AIzaSyDMeFOnOflzYJ-cjedJ8ky9AE-yThcNXFk')
        self.gemini_model = genai.GenerativeModel(
            'gemini-pro')
        self.blip_processor = AutoProcessor.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )
        self.blip_model = BlipForConditionalGeneration.from_pretrained(
            "Salesforce/blip-image-captioning-base"
        )

    def process_image(self, image_data):
        """
        Private method to resize and prepare the image for caption generation.

        :param image_data: PIL.Image - Image to process.
        :return: Tensor - Processed image tensor suitable for BLIP model.
        """
        transform = transforms.Resize((1080, 1080))
        processed_image = transform(image_data).convert("RGB")
        return processed_image

    def predict(self, image_data):
        """
        Generate five Instagram captions for the provided image.
        The image is first processed before generating captions.

        :param image_data: PIL.Image - The image for which captions are to be generated.
        :return: str - Five Instagram captions formatted as specified.
        """
        # Process image
        processed_image = self.process_image(image_data)
        inputs = self.blip_processor(images=processed_image, return_tensors="pt")
        generated_ids = self.blip_model.generate(**inputs, max_new_tokens=100, max_length=100)
        initial_caption = self.blip_processor.batch_decode(generated_ids, skip_special_tokens=True)

        # Generate Instagram captions using Gemini model
        prompt = (
            f"Given the provided photo caption, generate five distinct "
            f"and engaging Instagram captions. Each caption must include "
            f"at least one emoji and one hashtag. The captions should be "
            f"formatted with a preceding 'Caption #', followed by the "
            f"caption text. Ensure each caption is separated by a blank "
            f"line for readability.\n\n"
            f"Original Caption: {initial_caption}\n\n"
            f"Please format your response as follows:\n"
            f"**Caption 1**: [caption text] \n"
            f"**Caption 2**: [caption text] \n"
            f"**Caption 3**: [caption text] \n"
            f"**Caption 4**: [caption text] \n"
            f"**Caption 5**: [caption text] \n"
        )

        response = self.gemini_model.generate_content(prompt)
        return response.parts[0].text

# Usage
# generator = InstagramCaptionGenerator()
# img = Image.open('path_to_image.jpg').convert('RGB')
# captions = generator.import_and_predict(img)
# print(captions)
