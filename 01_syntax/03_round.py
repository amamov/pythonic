# round : 사사오입 반올림
# 반올림할 자리의 수가 5이면 반올림할 때,
# 앞자리의 숫자가 짝수이면 숫자 자체를 내림하고 홀수이면 숫자 자체를 올림한다.

print(round(3.14))  # 3
print(round(3.7))  # 4
print(round(3.5))  # 4
print(round(4.5))  # 4
print(round(-3.5))  # -4
print(round(-6.5))  # -6
print(round(4.675, 2))  # float인 경우는 예상과 다를 수 있다.

# int()는 소숫점을 그냥 버리고 정수형으로 타입을 변경한다.

x = 1.45
y = 1.35
z = 1.37
l = 1.32

# 사사오입 원칙을 따른다.
print("%.1f" % (x))  # 1.4
print("%.1f" % (y))  # 1.4
print("%.1f" % (z))  # 1.4
print("%.1f" % (l))  # 1.3