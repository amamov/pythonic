#### list : 수정이 가능하고(mutable) 순회 가능한 sequence
#### 순서(O), 중복(O), 수정(O), 삭제(O)

"""
del my_list[index]

.append(value)
.extend(list)
.remove(value)
.pop()
.insert(index, value)
.reverse()
.sort()
.index(value)
.count(value)

len(my_list)
sum(my_list)
max(my_list)
min(my_list)
"""


x = [1, 2, 3]
x[0] = 7  # 리스트 요소 수정
print(x)
# [7, 2, 3]

print(x[::-1])  # reversed
x[1:3] = [10, 20]
print(x)  # [7, 10. 20]

matrix = [[1, 2], [3, 4]]
print(matrix[1][0])
# 3
print(matrix[1][:])
# [3,4]

a = [3, 5]
b = [4, 7]
print(a + b)  # 여기서 +는 연결연산자이다.
# [3,5,4,7]
print(a * 3)  # a+a+a
# [3,5,3,5,3,5]

print(list("abc"))
# ['a', 'b', 'c']

print(list(range(1, 3)))
# [1, 2]

print(list((5, 6, 7)))
# [5, 6, 7]


print(
    "########################################################################################"
)
my_list = [2, 3, 5, 7, 11, 13]

#### myList.append( 추가할 값 ) : 리스트에 값을 추가한다. (추가)
my_list.append(15)
print(my_list)

#### myList.extend( 추가할 리스트 ) : 리스트에 리스트를 더한다. (연장)
my_list.extend([1000, 2000])
print(my_list)

#### myList.remove( 삭제할 값 ) : 원소를 지정하여 삭제 (제거)
my_list.remove(1000)
print(my_list)

#### del myList[지울 인덱스 번호] : index를 이용하여 삭제 (제거)
del my_list[1]
print(my_list)

#### myList.pop() : 맨 마지막에 있는 원소를 꺼내서 제거한다. (stack)
my_list.pop()
print(my_list)

#### myList.insert(n, x) : 리스트의 n번째 위치에 x를 삽입; n번째 요소는 뒤로 밀려난다. (수정)
my_list.insert(0, 100)
print("insert : ", my_list)
# [100, 2, 5, 7, 11, 13, 15]

# myList.reverse( ) : 리스트를 내림차순으로 정렬시킨다.(자료형이 문자일경우 알파벳 순서대로)
my_list.reverse()
print(my_list)

# myList.sort( ) : 리스트를 순서대로(오름차순) 정렬시킨다.(자료형이 문자일 경우 알파벳 순서대로)
my_list.sort()
print(my_list)

# myList.index(원소) : 해당 원소의 순서(index number)를 알 수 있다.
index_number = my_list.index(100)
print(index_number)

# len(myList) : 리스트의 원소의 개수를 구한다.
length = len(my_list)
print(length)

# myList.count( 특정 원소 ) : 리스트의 특정 원소의 개수를 구한다.
count = my_list.count(2)
print(count)

# sum(myList) : 리스트가 숫자일 경우, 원소들의 총합을 반환한다.
print(sum(my_list))

# max(myList) : 가장 큰 원소를 리턴한다.
print(max(my_list))

# min(myList) : 가장 작은 원소를 리턴한다.
print(min(my_list))