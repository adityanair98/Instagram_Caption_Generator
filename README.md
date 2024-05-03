# InstaMuse 🌟📸

<p align="center">
  <kbd><img src="insta.png" width=300></img></kbd>
</p>

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Technologies Used](#technologies-used)
- [Contributors](#contributors)

## Project Overview
<div>
    <p> Welcome to InstaMuse, your go-to tool for generating captivating captions for your Instagram posts! InstaMuse utilizes advanced natural language processing and computer vision algorithms to analyze your images and generate personalized captions tailored to your content. </p>
    <p> Struggling to find the perfect words to match your pictures? Let InstaMuse do the heavy lifting! With just a simple upload, our app analyzes your image and generate a witty, engaging, or inspiring caption that captures the essence of your moment.</p>
    <p>Whether you’re a selfie savant, a nature explorer, or a foodie fanatic, InstaMuse is here to amplify your Instagram presence. Jazz up your feed with tailored captions that resonate with your followers and attract new eyes to your profile. It’s quick, easy, and fun!</p>
</div>

## Dataset Description
We have compiled a comprehensive dataset by leveraging web scraping techniques with Selenium and complemented it with existing data from <a href="https://www.kaggle.com/datasets/prithvijaunjale/instagram-images-with-captions">Kaggle</a>. At present, we've successfully scraped data from a limited set of 10 profiles. While this initial dataset offers valuable insights, we recognize the potential for further enrichment and expansion when it comes to fine-tuning.

## Features 
- Image analysis using the <a href="https://huggingface.co/Salesforce/blip-image-captioning-large">BLIP</a> model.
- Caption generation based on image features and context using <a href="https://deepmind.google/technologies/gemini/#introduction">Gemini</a>.
- Customization options to tailor captions to your style and preferences.
- Hosted on Hugging Face Streamlit Spaces for seamless user experience.

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
streamlit run app.py
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
