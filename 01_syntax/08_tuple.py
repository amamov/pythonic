#### tuple : 수정이 불가능하고(immutable) 순회 가능한 sequence
#### 순서(O), 중복(O), 수정(X), 삭제(X)
#### tuple은 절대 바꾸지 않고 싶은 자료를 저장할 때 사용한다. 또한 tuple로 자료를 만들면 list보다 더 빠르게 컴퓨터가 읽고 불러올 수 있다.

my_tuple_1 = ()
my_tuple_2 = (1, 2)

t1 = (1, 2, 3, ["a", 7])
print(t1, type(t1))  # (1, 2, 3, ['a', 7]), <type 'tuple'>
print(t1[0])  # 1
print(t1[3][0])  # a
print(t1[0:2])  # (1, 2)

t2 = (4, 5)
print(t1 + t2)  # (1, 2, 3, ['a', 7], 4, 5)
print(t2 * 2)  # (4, 5, 4, 5)

##########################################################################################
t3 = 2, 3, 4  # Packing
print(t3, type(t3))  # (2, 3, 4), <type 'tuple'>

n1, n2, n3 = t3  # Unpacking
print(n1, type(n1))  # 2 <type 'int'>
print(n3)  # 4

n1, n2 = n2, n1  ##### tuple에서 자료를 수정하려면 Unpacking해야 한다.
print(n1, n2)  # 3 2
