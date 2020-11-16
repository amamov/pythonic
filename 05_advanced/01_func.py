def factorial(n: int) -> int:
    """ factorial function """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


class Example:
    pass


print(type(factorial), type(Example))
# <class 'function'> <class 'type'>

print(set(dir(factorial)) - set(dir(Example)))
# {'__code__', '__kwdefaults__', '__qualname__', '__name__', '__call__', '__defaults__', '__globals__', '__get__', '__annotations__', '__closure__'}

print(factorial.__name__)
print(factorial.__code__)

## 변수 할당
var_func = factorial
print(var_func)
print(var_func(5))

print(list(map(factorial, range(1, 6))))

print(list(map(factorial, filter(lambda x: x % 2 == 0, range(1, 6)))))
print([factorial(i) for i in range(1, 6) if i % 2 == 0])

# 인스 고정
from functools import partial

mul = lambda a, b: a * b

print(mul(3, 6))  # 18

# 첫번째 인자에 3 고정
three = partial(mul, 3)
print(three(3))  # 15
