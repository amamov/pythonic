## 코루틴에 값 전송하기


def number_coroutine():
    while True:  # 코루틴을 유지하기 위해 무한 루프 사용
        x = yield  # 코루틴 바깥에서 값을 받아온다.
        print(x)


co = number_coroutine()
next(co)  # 코루틴 안의 yield 까지 코드 실행(최초 실행)

co.send(1)  # 코루틴에 숫자 1을 보낸다.
co.send(2)  # 코루틴에 숫자 2를 보낸다.
co.send(3)  # 코루틴에 숫자 3을 보낸다.


## 코루틴 바깥으로 값 전달하기


def sum_coroutine():
    term, total = 0, 0
    while True:
        term = yield total  # 외부에서 코루틴으로 term을 받아오고 외부로 total을 보낸다.
        total += term


co = sum_coroutine()
print(next(co))  # 코루틴 안의 yield 까지 코드를 실행하고 코루틴에서 나온 값 출력

print(co.send(100))  # 코루틴에 100을 보내고 코루틴에서 나온 값 출력 (다음 yield 전 까지 계산됨)
print(co.send(200))  # 코루틴에 200을 보내고 코루틴에서 나온 값 출력


## 코루틴 종료 && 데코레이터로 코루틴 최초 실행 자동으로 하기


def coroutine(func):
    """ Coroutine decorator  """

    def inner(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return inner


@coroutine
def number_coroutine():
    try:
        while True:  # 코루틴을 유지하기 위해 무한 루프 사용
            x = yield  # 코루틴 바깥에서 값을 받아온다.
            print(x, end=" ")
    except GeneratorExit:
        print()
        print("코루틴 종료")


co = number_coroutine()

for i in range(10):
    co.send(i)

co.close()

# co.send(1) # error


@coroutine
def average_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        cnt += 1
        avg = total / cnt
    return avg


avg = average_re()

avg.send(10)
avg.send(30)
avg.send(50)

try:
    avg.send(None)
except StopIteration as e:
    print(e.value)