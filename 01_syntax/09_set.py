#### set : 데이터의 중복이 없고 순서가 없다. 데이터의 중복을 확인할때 주로 많이 사용하는 자료형이다.
#### 순서(X), 중복(X), 수정(O), 삭제(O)

"""
교집합 연산 : &  ex) set1 & set2
합집합 연산 : |  ex) set1 | set2
차집합 연산 : -
"""

my_set_1 = set((1, 2, 3))
my_set_2 = set((3, 4, 5))

print(my_set_1)  # {1, 2, 3}

print(my_set_1 & my_set_2)  # {3}

print(my_set_1 | my_set_2)  # {1, 2, 3, 4, 5}

print(my_set_1 - my_set_2)  # {1, 2}

# 추가
my_set_1.add(18)
print(my_set_1)  # {18, 1, 2, 3}

# 제거
my_set_1.remove(18)
print(my_set_1)  # {1, 2, 3}