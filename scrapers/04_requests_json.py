import json
import requests

"""
[용어 정리]
유니코드(Unicode) : 전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 설계된 산업 표준이다.
UTF-8 : 유니코드를 위한 가변 길이 문자 인코딩 방식 중 하나이고 유니코드 한 문자를 나타내기 위해 1바이트에서 4바이트까지 사용한다.
stream : 순서대로 물 흐르듯이 전송되는 데이터 Column
encode : code화하다.
decode : code를 원래 모습으로 바꾸다.
"""

data1 = []
response_dics = requests.get("https://nghttp2.org/httpbin/stream/3", stream=True)
# {'key1':'value1'}, {'key2':'value2'}, {'key3':'value3'},...

data2 = []
response_list = requests.get("https://jsonplaceholder.typicode.com/users", stream=True)
# [{'key1':'value1'}, {'key2':'value2'}, {'key3':'value3'},...]


def check_encoding(response):
    """ Encoding 확인 """
    print(f"Before Encoding : {response.encoding}")
    if response.encoding is None:
        response.encoding = "UTF-8"
    print(f"After Encoding : {response.encoding}")


check_encoding(response_dics)
check_encoding(response_list)

for line in response_dics.iter_lines(decode_unicode=True):
    # print(type(line)) # str
    # 한줄씩 JSON (DICT) 변환
    json_line = json.loads(line)
    # print(json_line)
    # print(type(json_line))
    data1.append(json_line)

data2 = response_list.json()

print(data1)
print("------------------------------")
print(data2)