### with : 파일 읽기 쓰기
"""
1. 읽기 모드 : r 
2. 쓰기 모드(기존 파일을 덮어쓴다.) : w
3. 추가 모드(파일 생성 및 추가) : a
"""

### [읽기]
file = open("./test_files/test.txt", "r")
content = file.read()
print(content)
# 반드시 close 리소스 반환
file.close()

print("-----------------------------------------")

# with문을 사용하면 close가 없어도 with 블럭이 끝나면 자동으로 리소스를 반환한다.
with open("./test_files/test.txt", "r") as file:
    line = file.readline()
    print(">", line)

    content = file.read()
    print(">", content)

    content = file.read()  # cursor가 끝으로 가서 내용이 없음
    print(">", content)

print("-----------------------------------------")

with open("./test_files/test.txt", "r") as file:
    lines = file.readlines()
    print(">", lines)  # list

# [쓰기]
with open("./test_files/test2.txt", "w") as f:
    file.write("wow!!")
    print("txt에 log 할 수 있다!!", file=f)

# [추가]
with open("./test_files/test2.txt", "a") as file:
    file.write("wow!! 파일에 추가하였다!!")


# [json 파일 만들기]
import json

dic = {"name": "joy", "2": "2"}

with open("./test_files/test.json", "w", encoding="utf-8") as file:
    json.dump(dic, file, indent="\t")
