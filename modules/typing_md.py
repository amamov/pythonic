# [typing] : 외장 모듈

# 자료형의 타입을 느슨하게 검사할 수 있다.
# 엄격하게 잡지는 않고 타입 주석이에 가깝다.

from typing import List, Callable


def add(x: List[int]) -> int:
    return sum(x)


print(add([1, 2, 3]))
print(add((1, 2, 3, 4)))  # 튜플도 같이 작동한다.

# Callable : 함수를 넘길 떄 사용한다.
def plus(a: int, b: int) -> float:
    return a / b


def call_func(a: int, b: int, func: Callable[[int, int], float]) -> float:
    return func(a, b)


print(call_func(10, 18, plus))