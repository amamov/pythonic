"""
    nodemon pg.py
"""


def check_expression(n: str) -> str:
    pass


cal1 = "1+2+3"
cal2 = "1+2*3"
cal3 = "1+((2))"
cal4 = "1+((2"
cal5 = ""

print(eval(check_expression(cal1)))