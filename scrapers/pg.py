import requests
from bs4 import BeautifulSoup

"""
세션(session)이란 웹 사이트의 여러 페이지에 걸쳐 사용되는 사용자 정보를 저장하는 방법을 의미한다.
사용자가 브라우저를 닫아 서버와의 연결을 끝내는 시점까지를 세션이라고 한다.
"""

LOGUN_INFO = {
    "userid": "danny5336",
    "password": "neo80557@",
}

# 세션 with 구문 안에서 유지 활성화
with requests.Session() as session:
    session = requests.Session()

    # http get request
    request = session.get(
        "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com"
    )

    # html 소스 가져오기
    html = request.text
    soup = BeautifulSoup(html, "html.parser")

    # http header 가져오기
    header = request.headers

    # http status 가져오기 (수신 상태 코드)
    status_code = request.status_code

    # http 수신 상태 확인
    is_ok = request.ok
