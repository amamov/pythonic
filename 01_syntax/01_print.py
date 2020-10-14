print("fcking world")  # fcking world

# [연결연산자]
print("ama" + "mov" + " 1205")  # amamov 1205

# [end=""]
print("sangseok", end=" sexy")  # sangseok sexy
for i in range(1, 5):
    print(i, end=" ")
# 1 2 3 4

# [sep=""]
print(1, 2, 3, sep="x")
# 1x2x3x

# [문자열 띄어쓰기는 콤마로 가능하다.]
print(1, 2, 3)  # 1 2 3

# [\n]
print("sangseok\nyerim")
# sangseok
# yerim

# [\t]
print("sangseok\tyerim")
# sangseok	yerim

# [python에는 한줄에 하나의 코드를 쓴다.]
# [한 줄에 두 개 이상의 코드를 쓰고 싶으면 ;를 이용한다.]
print("sangseok")
print("love")
# sangseok
# love

# [f-string] (python 3)
name = "amamov"
age = 23
print(f"{name}'s age is {age}")
# amamov's age is 23

# ["{}".format(x)]
a = 3
print("a는 {}이다.".format(a))
# a는 3이다.

# ["%"%(x)]
print("%10s%10s%10s" % ("item", "count", "price"))
#      item     count     price

print("%6d" % (123456))
print("%6.2f" % (12.12345))
# 123456
# 12.12
