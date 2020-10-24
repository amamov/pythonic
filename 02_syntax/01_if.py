n = int(input("Enter the number : "))

if n % 2 == 0 and n % 3 == 0:
    print(n, " is divisible by 2 and 3.")
elif n % 2 == 0 or n % 3 == 0:
    print(n, " is divisible by 2 or 3.")
elif (n % 2 == 0 or n % 3 == 0) and not (n % 2 == 0 and n % 3 == 0):
    print(n, " is divisible by 2 or 3, but not both.")
else:
    print("wow !")


# Enter the number : 3
# 3  is divisible by 2 or 3.

### 삼항 연산자
number1 = 1
number2 = 2
number3 = 3

# 1. and-or : 인터프리터의 원리를 이용한 문법 -> 오류가 존재할 수 있다. 5==5 and 5-5 or 5+5 -->10(오류)
result1 = (number2 > number1) and "1은 2보다 작다" or "1은 2보다 크다."

# 2. if-else : 권장되는 삼항 연산자
result2 = "3은 2보다 크다" if number3 > number2 else "3은 2보다 작다."

print(result1)
# 1은 2보다 작다

print(result2)
# 3은 2보다 크다
