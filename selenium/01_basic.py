from selenium import webdriver
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DRIVERS_DIR = BASE_DIR / "drivers"
CHROMEDRIVER_PATH = str(DRIVERS_DIR / "chromedriver")

browser = webdriver.Chrome(CHROMEDRIVER_PATH)
print(dir(browser))

## [브라우저 내부 대기 (인터넷 환경에 따라 대기를 시켜줘야한다.)]
# Implicitly wait을 10초로 설정하면 페이지가 로딩되는데 10초까지 기다린다.
# 만약 페이지 로딩이 2초에 완료되었다면 더 기다리지 않고 다음 코드를 수행한다.
# 기본 설정은 0초로 되어있고, 한번만 설정하면 driver를 사용하는 모든 코드에 적용이 된다.
browser.implicitly_wait(5)  # 5초 대기

## [브라우저 사이즈 제어]
# browser.set_window_size(1000, 500)  # 사이지 지정
browser.maximize_window()  # 가장 크게 브라우저를 연다
# browser.minimize_window()  # 가장 작게 브라우저를 연다.

## [페이지 이동]
browser.get("http://www.naver.com")

## [페이지 내용 (source)]
print(browser.page_source)

## [세션 값 출력]
print(browser.session_id)

## [타이틀 출력]
print(browser.title)

## [현재 URL 출력]
print(browser.current_url)

## [현재 쿠키 정보 출력]
print(browser.get_cookies())

## [검색하기 -> 스크린샷]
# element = browser.find_elements_by_css_selector('...')
element = browser.find_element_by_id("query")
print(dir(element))
element.send_keys("조이")  # <input />에 입력
element.submit()
browser.get_screenshot_as_file(str(BASE_DIR / "files" / "web.png"))

## [브라우저 종료]
browser.quit()