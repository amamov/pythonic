import os
from urllib.parse import quote_plus  # 아스키 코드로 변환
from urllib.request import urlretrieve  # url 다운로드
from pathlib import Path
from fake_useragent import UserAgent  # fake user 삽입
from bs4 import BeautifulSoup
import requests

BASE_DIR = Path(__file__).resolve().parent
SAVE_DIR = str(BASE_DIR / "files")

BASE_URL = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
JOY = "%EC%A1%B0%EC%9D%B4"
image_files = []

with requests.Session() as session:
    keyword = "아이유"
    quote = quote_plus(keyword)
    url = BASE_URL + quote
    # print(f"url : {url}")
    response = session.get(
        url,
        headers={
            "User-Agent": UserAgent().ie,
        },  # User-Agent 정보 fake user 삽입
    )

    # 폴더 생성 예외 처리
    try:
        if not (os.path.isdir(SAVE_DIR)):
            os.makedirs(SAVE_DIR)
    except OSError:
        print("Folder created failed.")
        raise RuntimeError("System Exit.")
    else:
        print("Folder is created!")

    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())
    img_list = soup.select("div.img_area > a > img")

    for idx, img in enumerate(img_list):
        # print(img.attrs) # 속성값 확인
        image_source = img["data-source"]
        # 저장 파일명
        filename = f"{SAVE_DIR}/{idx+1}.png"
        urlretrieve(image_source, filename)

print("Download secceeded!")
