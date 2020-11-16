from math import sin, cos

# f = x - 2*sin(x^2) 의 해를 구하시오
# f1 = (x1 - x2) f1'
# x2 = x1 - f1/f1'


def func(x):
    return x - 2 * sin(x ** 2)


def prime_func(x):
    return 1 - 4 * x * cos(x ** 2)


def newton_method(func, prime_func):
    x = float(input("Starting guess : "))
    MAX_ITERS = 30
    tolerance = 1e-8
    iterations = 0
    while (iterations < MAX_ITERS) and (abs(func(x)) > tolerance):
        x = x - func(x) / prime_func(x)
        iterations += 1
    if iterations == MAX_ITERS:
        return "No root found"
    else:
        return f"Root : {x} found in {iterations} iterations"


print(newton_method(func, prime_func))
