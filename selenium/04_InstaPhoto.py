import os
from pathlib import Path
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class InstaPhoto:

    """
    [InstaPhoto Class]
    Author : Yoon - Sang Seok
    Date : 2020.11.13
    """

    DEV_MODE = True
    BASE_URL = "https://www.instagram.com/explore/tags/"
    IMAGE_CONTAINER_SELECTOR = "div.v1Nh3"

    def __init__(self, keyword):
        self.keyword = keyword
        self.url = InstaPhoto.BASE_URL + quote_plus(self.keyword)
        self.images = {
            "developer": "Yoon - Sang Seok (ammaov)",
            "site": "instagram",
            "keyword": keyword.strip(),
            "src": [],
        }

    def __str__(self):
        return f"Instagram Photo Keyword : {self.keyword}"

    def scrape(self):
        if InstaPhoto.DEV_MODE:
            BASE_DIR = Path(__file__).resolve().parent
            CHROMEDRIVER_PATH = str(BASE_DIR / "drivers" / "chromedriver")
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            browser = webdriver.Chrome(CHROMEDRIVER_PATH, options=chrome_options)
        else:
            # Heroku에 배포할때
            chrome_options = webdriver.ChromeOptions()
            chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--no-sandbox")
            browser = webdriver.Chrome(
                executable_path=os.environ.get("CHROMEDRIVER_PATH"),
                chrome_options=chrome_options,
            )
        wait = WebDriverWait(browser, 30)
        browser.implicitly_wait(10)
        browser.get(self.url)
        try:
            wait.until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, InstaPhoto.IMAGE_CONTAINER_SELECTOR)
                )
            )
        except Exception as error:
            print(error)
        else:
            soup = BeautifulSoup(browser.page_source, "html.parser")
            img_list = soup.select(InstaPhoto.IMAGE_CONTAINER_SELECTOR + " img")
            for img in img_list:
                try:
                    self.images["src"].append(img["src"])
                except KeyError:
                    pass
        finally:
            browser.quit()


if __name__ == "__main__":
    photo = InstaPhoto("조이")
    photo.scrape()
    print(photo.images)
