# 다나와 자동 로그인


import requests
from fake_useragent import UserAgent

userid = input("아이디를 입력해주세요 : ")
password = input("비밀번호를 입력해주세요 : ")

# 로그인 정보 (개발자 도구)
login_info = {
    "redirectUrl": "http://www.danawa.com/",
    "loginMemberType": "general",
    "id": userid,
    "isSaveId": "false",
    "password": password,
}

headers = {
    "User-Agent": UserAgent().chrome,
    "Referer": "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F",
}

with requests.Session() as session:
    response = session.post(
        url="https://auth.danawa.com/login", data=login_info, headers=headers,
    )

    if not response.ok:
        raise Exception("Login failed!")

    # print(response.content.decode("UTF-8"))
    # print(response.text)

    response = session.get(
        "https://buyer.danawa.com/order/Order/orderList", headers=headers,
    )

    # euc-kr (한글이 깨질경우)
    # response.encoding = 'euc-kr'

    print(response.text)
