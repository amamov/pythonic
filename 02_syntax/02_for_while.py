# [for]

for i in range(5):
    print(i, end=" ")
print()

for i in range(0, 9, 2):
    print(i, end=" ")
print()

for i in range(0, -9, -2):
    print(i, end=" ")
print()
##### iterable 한 것들은 모두 순회 가능하다. : list, tuple, set, string, dictionary, ...

## list
my_list = [2, 3, 5, 7]

for i in my_list:
    print(i, end=" ")
print()

for idx, value in enumerate(my_list):
    print(idx, value)

## dictionary
my_dict = {
    "name": "amamov",
    "age": 23,
    "city": "Seoul",
}

for key in my_dict:
    print("key : ", key)

for values in my_dict.values():
    print("value : ", key)

for key in my_dict.keys():
    print("key : ", key)

for key, value in my_dict.items():
    print("key, value : ", key, value)

## set
my_set = set((2, 9, 3, 7, 1, 100, 1000))
for i in my_set:
    print(i)

######### enumerate #########
name = ["yoon", "kim", "lee"]
for idx, val in enumerate(name):
    print(idx, val)


######### list comprehention #########
squareNumbers = [x ** 2 for x in range(1, 11)]
print(squareNumbers)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

twiceNumbers = [2 * x for x in [1, 2, 3, 4, 5, 6]]
print(twiceNumbers)
# [2, 4, 6, 8, 10, 12]


myList = [2 * x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]
# [1, 2, 3, 4, 5, 6]에서 2의 배수들을 2배한 값들을 리스트로 리턴
print(myList)
# [4, 8, 12]

r = [i * j for i in range(1, 5) for j in range(1, 3)]
# for 문 중첩
print(r)  # [1, 2, 2, 4, 3, 6, 4, 8]

r = [i * j for i in range(1, 5) for j in range(1, 3) if i * j % 2]
print(r)  # [1, 3]


print("######################################################################")
# [while]
i = 0
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

flag = True
n = 0
while flag:
    n += 1
    print(n, end=" ")
    if n == 10:
        flag = False