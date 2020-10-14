number = input()
# 17(입력)
print(number)
# 17
print(type(number))
#  <class 'str'>
# input의 값의 결과 타입은 str 타입이다.

name = input("What your name? : ")
# What your name? : sangseok(입력)
print(name)
#'sangseok'

a, b = map(int, input("숫자를 입력하세요 : ").split(", "))
# 숫자를 입력하세요 : 1, 2(입력)
print(a, b, sep="\n")
# 1
# 2

A = list(map(int, input().split(" ")))
# 입력한 만큼 리스트로 반환된다.
print(A)

#######################################################
# input 은 속도가 느리므로 sys.stdin.readline( )을 사용하자.
import sys


# number0 = int(input())
# readline : 입력한 한 라인을 interable한 컨테이너에 저장한다.
readline = sys.stdin.readline()
print(readline)

# number1, number2 = map(int, input().split(" "))
number1, number2 = map(int, sys.stdin.readline().split(" "))

# numbers = list(map(int, input().split(" ")))
numbers = list(map(int, sys.stdin.readline().split(" ")))

# 여러줄 입력할 때
number_of_lines = int(input())
reads = [sys.stdin.readline() for i in range(number_of_lines)]
print(reads)