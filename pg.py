"""
    nodemon pg.py
"""
x = int(input())


def find_fraction(x: int) -> str:
    a, n = 1, 1
    while a < x:
        a += n + 1
        n += 1
    if n % 2 == 0:
        print(n - a + x, "/", a - x + 1, sep="")
    elif n % 2 != 0:
        print(a - x + 1, "/", n - a + x, sep="")


find_fraction(x)
