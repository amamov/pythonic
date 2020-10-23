#### Dictionary
# 변경할 수 없는 자료만 immutable(string, tuple, int 등)만 dictionary의 key가 될 수 있다.
# 순서(X), 중복(X), 수정(O), 삭제(O)
# dic={key1 : val1,  key2:  val2. ...]


"""
.keys()
.values()
.items()
.get(key, default)
"""

my_dic = {
    "name": "sang seok-Yoon",
    "age": 23,
}

print(my_dic)  # {'name': 'sang seok-Yoon', 'age': 23}
print(my_dic["name"])  # sang seok-Yoon
print(my_dic["age"])  # 23

### 자료 추가
my_dic["phone"] = "Iphone"
print(my_dic)
# {'name': 'sang seok-Yoon', 'age': 23, 'phone': 'Iphone'}

### 자료 삭제
del my_dic["phone"]  # Dictionary 자료 삭제
print(my_dic)
# {'name': 'sang seok-Yoon', 'age': 23}

my_dic_keys = my_dic.keys()
# 해당 Dictionary의 key 확인 keys()
print(my_dic_keys, type(my_dic_keys))
# dict_keys(['name', 'age']) <class 'dict_keys'>
print(tuple(my_dic_keys))
# ('name', 'age') : tuple로 변경가능
print(list(my_dic_keys))
# ['name', 'age'] : list로 변경가능

my_dic_values = my_dic.values()
# 해당 Dictionary의 key 확인 values()
print(my_dic_values)
# dict_values(['sang seok-Yoon', 23])

# kwy값과 그에 해당하는 value들의 쌍을 tuple로 리턴한다.
print(my_dic.items())
# dict_items([('name', 'sang seok-Yoon'), ('age', 23)])

print(my_dic.get("age"))  # 23
print(my_dic.get("phone", None))  # None

if "phone" in my_dic:  # NULL
    print("In")
else:
    print("NULL")

### key가 문자열일 경우 아래와 같이 정의할 수 있다.
my_dict_2 = dict(a=2, b=3, c=4)
print(my_dict_2)
# {'a': 2, 'b': 3, 'c': 4}