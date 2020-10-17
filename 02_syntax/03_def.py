#### 함수
"""
1. 함수의 선언 위치는 함수 호출보다 선행되어야 한다. 
2. 함수 또한 객체이므로 변수에 저장, 함수에 인자로 함수 전달 등이 가능하다.
3. Lambda식 표현 : 메모리 절약, 가독성 향상, 코드 간결 --> 함수는 객체 생성을 한다. (메모리 할당)
   But Lambda는 즉시 실행된다. (Heap 초기화; 메모리 초기화)

[전역변수 & 지역변수]
지역변수(Local variable)은 함수 안에서 정의 되는 변수이고 전역변수(Global variable)는 함수 밖에서 정의 되는 변수이다.

지역변수는 그 변수가 정의된 함수 안에서만 사용할 수 있다. 함수가 실행될 때마다 새로 만들어지고, 함수의 실행이 종료되면 삭제된다. 
지역변수를 이용해 그 데이터와 관련된 문제를 함수 내부의 문제로 국한시킬 수 있다. 

전역변수는 프로그램 어디서는 전역으로 사용할 수 있다. 하지만 함수 안에서 전역변수에 새로운 값을 대입할 수는 없다. 
파이썬에서 전역변수는 함수 안에서 읽을 수는 있지만 수정이 불가능하다.  

함수 안에서 전역변수를 수정할 수 없지만 global 문을 이용하면 전역변수를 함수 안에서 수정할 수 있다.
"""


def function(arg1, arg2, *args, **kwargs):
    print("arg1 : ", arg1)
    print("arg2 : ", arg2)

    print("args : ", args)
    print("args type : ", type(args))

    print("kwargs : ", kwargs)
    print("kwargs : ", type(kwargs))
    return arg1 + arg2


function(1, 2, 3, 4, 5, 6, 7, 8, 9, what=False, why=True, Fuck="Hello world!")
# arg1 :  1
# arg2 :  2
# args :  (3, 4, 5, 6, 7, 8, 9)
# args type :  <class 'tuple'>
# kwargs :  {'what': False, 'why': True, 'Fuck': 'Hello world!'}
# kwargs :  <class 'dict'>

#### 단일 파라미터는 다중 파라미터보다 먼저 와야한다.
def plus(number1, *number):
    return number1 + sum(number)


print(plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))  # 55


#### 초기값을 미리 설정할 수 있다.
def default_func(arg1, arg2, x=100, y=200):
    print("arg1 : ", arg1, end=", ")
    print("arg2 : ", arg2, end=", ")
    print("x : ", x, end=", ")
    print("y : ", y)


default_func(1, 3, 5)
# arg1 :  1, arg2 :  3, x :  5, y :  200
default_func(1, 3)
# arg1 :  1, arg2 :  3, x :  100, y :  200
default_func(1, 3, y=5, x=4)
# arg1 :  1, arg2 :  3, x :  4, y :  5

#### 중첩함수(클로저) : 함수 안에 있는 함수
def nested_func(arg):
    def func_in_func(arg):
        print(">> ", arg)

    print("in nested_func")
    func_in_func(arg + 100)


nested_func(100)  # 200

#### Hint
def print_hello_world(hello: str, count: int) -> list:
    return list(hello * count)


print(print_hello_world("fuck", 3))


#### Lambda식 표현
# 일반적인 함수
def mul_10(num: int) -> int:
    return num * 10


var_func = mul_10
print(var_func)  # <function mul_10 at 0x7fed96ec15f0> : 함수의 객체가 생성되어 메모리에 할당되었다.
print(type(var_func))  # <class 'function'>

# Lambda 함수
lambda_mul_10 = lambda num: num * 10
print(lambda_mul_10)  # <function <lambda> at 0x7f876258e3b0>
print(lambda_mul_10(10))  # 100
