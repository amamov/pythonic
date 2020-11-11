import os
import subprocess
from urllib.parse import quote_plus  # 아스키 코드로 변환
from urllib.request import urlretrieve  # url 다운로드
from pathlib import Path
from fake_useragent import UserAgent  # fake user 삽입
from bs4 import BeautifulSoup
import requests

BASE_DIR = Path(__file__).resolve().parent
SAVE_DIR = str(BASE_DIR / "images")
BASE_URL = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="


class PhotoScraper:
    def __init__(self, keyword):
        self.keyword = keyword
        self.quote = quote_plus(keyword)
        self.url = BASE_URL + self.quote

    def scrape(self):
        with requests.Session() as session:
            response = session.get(
                self.url,
                headers={
                    "User-Agent": UserAgent().chrome,
                },  # User-Agent 정보 fake user 삽입
            )
            try:
                if not (os.path.isdir(SAVE_DIR)):
                    os.makedirs(SAVE_DIR)
            except OSError:
                print("Folder created failed.")
                raise RuntimeError("System Exit.")
            else:
                print("Folder is created!")
                subprocess.Popen(["open", SAVE_DIR])  # 폴더 열기 (mac)
            soup = BeautifulSoup(response.text, "html.parser")
            img_list = soup.select("div.img_area > a > img")

            for idx, img in enumerate(img_list):
                # print(img.attrs) # 속성값 확인
                image_source = img["data-source"]
                filename = f"{SAVE_DIR}/{idx+1}.png"
                urlretrieve(image_source, filename)
            print("Download secceeded!")
