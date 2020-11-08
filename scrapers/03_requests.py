import requests

response = requests.get("https://www.google.com")
# print(response.text)

"""
세션(session)이란 웹 사이트의 여러 페이지에 걸쳐 사용되는 사용자 정보를 저장하는 방법을 의미한다.
사용자가 브라우저를 닫아 서버와의 연결을 끝내는 시점까지를 세션이라고 한다.
1. 서버는 세션 ID를 클라이언트가 웹사이트에 접속시 발급해준다.
2. 클라이언트는 서버에서 클라이언트로 발급해준 세션 ID를 쿠키를 사용해서 저장한다.
3. 클라이언트는 다시 접속시, 이 쿠키를 이용해서 세션 ID값을 서버에 전달합니다.
"""

# 세션 with 구문 안에서 유지 활성화 : 이 구문 안에서 session 동작을 진행할 수 있다.
with requests.Session() as session:
    session = requests.Session()

    # 쿠키 삽입
    jar = requests.cookies.RequestsCookieJar()
    jar.set("name", "amamov", domain="httpbin.org", path="/cookies")

    # http get request
    response = session.get(
        "https://httpbin.org/cookies",
        # cookies={"name": "amamov"},
        cookies=jar,  # 많은 정보의 쿠키를 저장할때 jar을 이용한다.
        timeout=2,  # 2초 동안 기다려준다.
    )

    # html 소스 가져오기
    html = response.text

    # http header 가져오기
    header = response.headers

    # http status 가져오기 (수신 상태 코드)
    status_code = response.status_code

    # http 수신 상태 확인
    is_ok = response.ok
