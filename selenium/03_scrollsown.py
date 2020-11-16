import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent
DRIVER_PATH = str(BASE_DIR / "drivers" / "chromedriver")
URL = "https://www.google.com/search?q=%EC%A1%B0%EC%9D%B4&sxsrf=ALeKk03zK5Crpl_wHjvjWfy3ZnaO5ATsaw:1605251573518&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjf4MGO_P7sAhUTHXAKHT8pDIcQ_AUoAXoECAUQAw&biw=1309&bih=683"

chrome_options = Options()
# chrome_options.add_argument("--headless")

browser = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
browser.implicitly_wait(4)
browser.maximize_window()
browser.get(URL)

# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# 스크롤 1000만큼 내리기
# browser.execute_script("window.scrollTo(0, 1000);")


# 현재 상태에서 1000만큼 쭉쭉 내리기
while True:
    browser.execute_script("window.scrollTo(0, window.scrollY + 1000);")
    time.sleep(1)
