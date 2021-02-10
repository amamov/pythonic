"""
Generator : iterator 객체의 한 종류이다.
제너레이터를 사용하면 메모리를 효율적으로 사용할 수 있다. sys.getsizeof()로 확인 가능하다.
sys.getsizeof(변수): 변수에 담긴 객체의 메모리 크기 정보를 반환하는 함수

[제너레이터를 만드는 방법]
1. Generator function
2. Generator expression

- 딕셔너리, 리스트 한 번 호출 할 때 마다 하나의 값만 리턴 -> 아주 적은 메모리 양을 필요로 함
"""

# 1. Generator function
# yield가 하나라도 들어가면 제너레이터가 된다.


def number_generator_func():
    print("first")
    yield 1  # 첫번째 next 호출에서 이 문장까지 실행된다.
    print("second")
    yield 2  # 두번째 next 호출에서 이 문장까지 실행된다.
    print("third")
    yield 3  # 세번째 next 호출에서 이 문장까지 실행된다.


number_generator = number_generator_func()
print(type(number_generator))
print(next(number_generator))
print(next(number_generator))


def for_generator_func():
    for i in [1, 2, 3, 4, 5]:
        yield i
    # loop = [1, 2, 3, 4, 5]
    # yield from loop


for_generator = for_generator_func()
print(next(for_generator))
print(next(for_generator))


# 2. Generator expression

g = (i for i in range(10))
print(type(g))
print(next(g))
print(next(g))
print(next(g))


# 제너레이터 객체


class WordSplitGenerator:
    def __init__(self, text):
        self.idx = 0
        self.text = text.split(" ")

    def __iter__(self):
        for word in self.text:
            yield word  # 제너레이터

    def __repr__(self):
        return f"WordSplit({self.text})"


wg = WordSplitGenerator("i love you baby")

wi_2 = iter(wg)

print(wi_2)
print(next(wi_2))
print(next(wi_2))


# 제너레이터 관련 패키지 함수

import itertools

gen1 = itertools.count(1, 2.5)  # 1부터 2.5씩 증가하면서 끝이 없는 제너레이터를 만든다.

# for i in gen1:
#     print(i) # 무한히 동작한다.

# 1부터 2.5씩 증가하면 서 100이하의 수들의 제너레이터를 만든다.
gen2 = itertools.takewhile(lambda n: n < 100, itertools.count(1, 2.5))

# 누적 합계
gen3 = itertools.accumulate(x for x in range(1, 100))

# for i in gen3:
#     print(i)
