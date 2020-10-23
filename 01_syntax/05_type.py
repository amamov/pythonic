# [Python의 기본적인 데이터 타입 종류]

"""
Boolean
Number
String
Bytes
Lists (집합 자료형)
Tuples (집합 자료형)
Sets (집합 자료형)
Dictionary (집합 자료형)
"""

my_str = "amamov"
my_bool = True
my_int = 17
my_float = 3.14
my_complex = complex(1, 2)
my_list = [2, 3, 5, 7, 11]
my_tuple = 1, 3, 5, 7
my_set = set((2, 4, 6, 8))
my_dict = {
    "name": "Yoon",
    "age": 23,
}


print(type(my_str))
# <class 'str'>

print(type(my_bool))
# <class 'bool'>

print(type(my_int))
# <class 'int'>

print(type(my_float))
# <class 'float'>

print(type(my_complex))
# <class 'complex'>

print(type(my_list))
# <class 'list'>

print(type(my_tuple))
# <class 'tuple'>

print(type(my_set))
# <class 'set'>

print(type(my_dict))
# <class 'dict'>

number_1 = 5.0
number_2 = 4
print(type(number_1), type(number_2), type(number_1 + number_2))

# 형변환
print(int(number_1))  # 5
print(float(number_2))  # 4.0
print(complex(number_2))  # 4+0j
print(int(True))  # 1
print(int(False))  # 0
print(int("3"))  # 3
