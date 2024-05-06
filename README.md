# InstaMuse 🌟📸

<p align="center">
  <kbd><img src="insta.png" width=300></img></kbd>
</p>

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Repository Description](#repository-description)
- [Usage](#usage)
- [Installation](#installation)
- [Technologies Used](#technologies-used)
- [Contributors](#contributors)

## Project Overview

This repository contains the source code for InstaMuse, a Streamlit app that generates captions for Instagram posts based on the content of the uploaded image. The app uses the BLIP model for image captioning and the Gemini model for generating captions based on the image features and context. The app allows users to upload an image, view the generated captions, customize the captions, and copy the selected caption for use in their Instagram posts..

The app is hosted on Hugging Face Streamlit Spaces, making it easily accessible to users. The user-friendly interface allows users to quickly generate captions for their Instagram posts, helping them save time and effort. The app is designed to provide users with high-quality captions that are tailored to their style and preferences, making it a valuable tool for content creators and social media influencers.

**App Link:** https://huggingface.co/spaces/witchEverly/InstaMuse-Caption-Generator


## Features 
- Image analysis using the <a href="https://huggingface.co/Salesforce/blip-image-captioning-large">BLIP</a> model.
- Caption generation based on image features and context using <a href="https://deepmind.google/technologies/gemini/#introduction">Gemini</a>.
- Customization options to tailor captions to your style and preferences.
- Hosted on Hugging Face Streamlit Spaces for seamless user experience.
- Easy-to-use interface for quick and efficient caption generation.

## Repository Description

This repository contains the code for the InstaMuse application, which is a Streamlit app that generates captions for Instagram posts based on the content of the uploaded image. The app uses the BLIP model for image captioning and the Gemini model for generating captions based on the image features and context. The app allows users to upload an image, view the generated captions, customize the captions, and copy the selected caption for use in their Instagram posts.
Please find the repository structure below:

```
├── Instagram_Caption_Generator/         # Root directory of the
│   ├── analyses/                        # Folder containing the analysis notebooks
│   │   ├── BLIP_Image_Captioning.ipynb  # Notebook for image captioning using BLIP
│   ├── application/                     # Folder containing the Streamlit application
│   │   ├── images/                      # Folder containing images used in the application
│   │   ├── pages/                       # Folder containing the different pages of the application
│   │   │   ├── 📸_InstaMuse.py          # Main Streamlit application
│   │   ├── user_data/                   # Folder containing user-uploaded images
│   │   ├── app_utils.py                 # Utility functions for the Streamlit application
│   │   ├── CaptionGenerator.py          # Class for generating captions
│   │   ├── test.py                      # Test file for the CaptionGenerator class
│   │   ├── ✨_Home.py                   # Home page of the Streamlit application
│   ├── scratch/                         # Folder containing scratch / obsolete files
│   ├── .gitignore                       # Standard template for .gitignore file
│   ├── README.md                        # Readme file for the repository
│   ├── requirements.txt                 # File containing the required packages
```

## Usage
**App Link: [InstaMuse](https://huggingface.co/spaces/witchEverly/test)**

1. Upload Your Photo:
    - Visit our InstaMuse space on Hugging Face Streamlit Spaces.
    - Click on the upload button to select the image you want to generate a caption for.
2. Explore Caption Options:
    - Once the image is uploaded, InstaMuse will analyze it and present you with five caption options.
    - Explore each option to find the caption that best suits your photo and personal style.
3. Customize and Refine:
    - Feel free to customize the selected caption to better align with your preferences.
    - Edit the caption text or add your own personal touch to make it uniquely yours.
4. Share Your Creations:
    - Once you're satisfied with your caption, copy it and paste it into your Instagram post.
    - Share your photo with your followers and watch as they engage with your captivating content!

## Installation
To run the app locally, follow these steps:
1. Clone the repository:
```bash
git clone https://github.com/adityanair98/Instagram_Caption_Generator
```
2. Change the directory:
```bash
cd Instagram_Caption_Generator
```
3. Install the required packages:
```bash
pip install -r requirements.txt
```
4. Run the Streamlit app:
```bash
streamlit run application/pages/📸_InstaMuse.py
```

## Technologies Used
- Python
- PyTorch
- Hugging Face
- Streamlit
- Selenium
- HTML/CSS

## Contributors
- [Aditya Nair](https://github.com/adityanair98)
- [Bhumika Srinivas](https://github.com/bhumikasrc)
- [Cassie Richter](https://github.com/cjrich19)
- [Jessica Brungard](https://github.com/witchEverly)
- [Seneth Waterman](https://github.com/seneth-waterman)
