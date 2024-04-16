from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import pathlib
import pickle
import pandas as pd
import time



def scraper():
    public_profiles = pd.read_csv('data/data.csv')
    usernames = list(public_profiles['name'])
    df = pd.DataFrame(columns=['image', 'caption'])

    for username in usernames:
        try:
            website = f"https://www.instagram.com/{username}/?hl=en"
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            driver.maximize_window()
            driver.get(website)
            time.sleep(10)

            frame3x4 = driver.find_elements(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/div[3]/article')
            sections = frame3x4[0].find_elements(By.XPATH, './div/div/div')
            posts = []
            for section in sections:
                for post in section.find_elements(By.XPATH, './div/a'):
                    posts.append(post)
        except Exception as e:
            print(f"Failed to scrape {username}")
            print("Error:", e)
            driver.quit()
            continue

        images = []
        captions = []
        for post in posts:
            img = post.find_elements(By.XPATH, './div[1]/div[1]/img')
            if len(img) == 0:
                print(post.get_attribute('innerHTML'))
            else:
                img_url = img[0].get_attribute('src')
                img_alt = img[0].get_attribute('alt')
                img_alt = "\n".join([line for line in img_alt.splitlines() if line.strip()])
                images.append(img_url)
                captions.append(img_alt)

        df = pd.concat([df, pd.DataFrame({'image': images, 'caption': captions})], ignore_index=True)
        driver.quit()
        time.sleep(5)

    df.to_csv('data/public_profiles.csv', index=False)


if __name__ == '__main__':
    scraper()
