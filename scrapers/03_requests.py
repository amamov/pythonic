import requests

"""
세션(session)이란 웹 사이트의 여러 페이지에 걸쳐 사용되는 사용자 정보를 저장하는 방법을 의미한다.
사용자가 브라우저를 닫아 서버와의 연결을 끝내는 시점까지를 세션이라고 한다.
1. 서버는 세션 ID를 클라이언트가 웹사이트에 접속시 발급해준다.
2. 클라이언트는 서버에서 클라이언트로 발급해준 세션 ID를 쿠키를 사용해서 저장한다.
3. 클라이언트는 다시 접속시, 이 쿠키를 이용해서 세션 ID값을 서버에 전달합니다.
"""

URL = "https://httpbin.org"

# 세션 with 구문 안에서 유지 활성화 : 이 구문 안에서 session 동작을 진행할 수 있다.
with requests.Session() as session:

    # cookie return : 클라가 서버에게 보낸 쿠키를 서버가 확인하고 다시 클라한테 보내주는 코드 (서버에 저장 x)
    response1 = session.get(url=f"{URL}/cookies", cookies={"name": "amamov"})
    print(response1.text)

    # cookie set : 서버에 쿠키를 저장
    response2 = session.get(url=f"{URL}/cookies/set", cookies={"name": "amamov"})
    print(response2.text)

    # http header 가져오기
    header = response2.headers

    # http status 가져오기 (수신 상태 코드)
    status_code = response2.status_code

    # http 수신 상태 확인
    is_ok = response2.ok

    # User-Agent header 전송
    headers = {"user-agent": "nice-man_1.0.0_mac_book_wow_chrome"}
    response3 = session.get(url=URL, headers=headers)
    print(response3.text)
