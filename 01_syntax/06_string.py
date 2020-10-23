#### str : 한번 선언하면 수정이 불가능하고(immutable) 순회 가능한 sequence

"""
.strip()
.replace(old, new, count)
.find(value)
.count(value)
.upper()
.lower()
.split()
.join(list or str or ...)
"""

escape_str = 'Hello "my Name is amamov "'
print(escape_str)
# Hello "my Name is amamov "

#### Raw String (그대로 출력한다.)
raw_s1 = r"C:\pgograms\t\fuck\n\wow"
print(raw_s1)
# C:\pgograms\t\fuck\n\wow

#### 멀티 라인
multi = """
문자열

멀티라인
"""

#### my_str[start:end:step] start 인덱스부터 end 인덱스 바로 전까지 step만큼 건너뛰며 출력한다.
my_name = "sangseok"

print(my_name[1:3])
# an
print(my_name[::2])
# snso
print(my_name[::-1])  # 문자열 거꾸로 바꾸기
# koesgnas
print(my_name[:])
# sangseok

my_str = " amamov "

#### split() : 문자열을 나눈다.(문자열을 리스트로 변환)
print(my_str.split())  # ['amamov']
print(my_str.split("a"))  # ['', 'm', 'mov']

#### strip() : 인자로 전달된 문자를 my_str의 왼쪽과 오른쪽에서 제거한다. (공백을 제거할 때 많이 쓰인다.)
print(my_str.strip())  # 공백이 제거된 문자열을 반환한다.
# amamov

#### replace(old, new, count) : 수정된 문자열을 반환한다.
print(my_str.replace("a", "x", 1))  #  xmamov
print(my_str.replace("a", "x", 2))  #  xmxmov

#### find("특정 문자") : 특정 문자의 인덱스를 반환한다.
print(my_str.find("a"))  # 1

#### len(my_str) : 문자열의 글자 수를 리턴한다.
print(len(my_str))  # 8

#### count('원하는 문자') : 원하는 문자 수를 리턴한다.
print(my_str.count("a"))  # 2

#### upper() : 문자열의 소문자를 대문자로 바꾼다.
print(my_str.upper())  #  AMAMOV

#### lower() : 문자열의 대문자를 소문자로 바꾼다.

#### join
print("amamov".join("ss"))  # samamovs

# list -> str
print("".join(["1", "2", "3"]))  # 123
