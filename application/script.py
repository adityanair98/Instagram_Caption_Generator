"""
This script is used to generate Instagram captions for a given image. The script
imports the necessary libraries and initializes the models required for caption
generation. The `import_and_predict` function takes an image as input and returns
five possible Instagram captions for the image. The script also includes a snippet
for debugging purposes, where an image is loaded and captions are generated for it.
"""
from os import getenv
from dotenv import load_dotenv
import google.generativeai as genai
from transformers import AutoProcessor, BlipForConditionalGeneration
from torchvision import transforms

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
    This function takes an image as input and generates five Instagram captions
    by first generating a BLIP description for the image and then using the Gemini
    model to generate Instagram captions based on the BLIP description.

    :param image_data: PIL.Image - The image for which captions are to be generated
    :return: response: str - Five Instagram captions for the given image
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


# Uncomment and import necessary libraries to run this test code:
# PATH = "~/Desktop/Misc/img_5223.jpeg"
# img_path = expanduser(PATH)
# image = Image.open(img_path).convert('RGB')
