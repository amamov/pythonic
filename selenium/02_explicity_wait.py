import time
from pathlib import Path
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  # 기대 상태
from selenium.webdriver.common.by import By  # 기다릴때

BASE_DIR = Path(__file__).resolve().parent
DRIVER_PATH = str(BASE_DIR / "drivers" / "chromedriver")
URL = "http://prod.danawa.com/list/?cate=112758&15main_11_02"

chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저가 실행되지 않는다.

# webdriver 설정(headless 모드)
browser = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
# browser = webdriver.Chrome(DRIVER_PATH)

browser.implicitly_wait(5)
browser.set_window_size(1000, 1000)
browser.get(URL)
# print(browser.page_source)


## 제조사별 더 보기 클릭 - Explicity wait
# browser를 3초동안 기다린다.
# 3초 안에 내가 선택하려고 하는 요소가 랜더링되면 클릭을 하고 3초 안에 나타지 않으면 에러를 리턴한다.
WebDriverWait(browser, 3).until(
    expected_conditions.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]',
        )
    )
).click()

## 제조사별 더 보기 클릭 - Implicity wait (안좋은 코드)
# time.sleep(2)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

## APPLE 버튼 클릭
WebDriverWait(browser, 2).until(
    expected_conditions.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="selectMaker_simple_priceCompare_A"]/li[13]/label',
        )
    )
).click()

time.sleep(2)

soup = BeautifulSoup(browser.page_source, "html.parser")
product_list = soup.select("ul.product_list > li.prod_item > div.prod_main_info")
for product in product_list:
    a = product.select_one("div.prod_info > p.prod_name > a").text.strip()
    print(a)

browser.quit()
