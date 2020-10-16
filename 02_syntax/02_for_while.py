# [for]
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
ab_sum = []

for i in b:
    for j in a:
        ab_sum.append(i + j)

print(ab_sum)

for i in range(5):
    print(i, end=" ")
print()

for i in range(0, 9, 2):
    print(i, end=" ")
print()

for i in range(0, -9, -2):
    print(i, end=" ")
print()

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


######################################################################
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
