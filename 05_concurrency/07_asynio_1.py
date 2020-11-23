# Block I/O : 한 요청을 할때 모든 스레드가 멈춰있는 것이다. 즉, 한 명이 일을 끝내지 않으면 일을 할 수 없는 상태(순차 실행)
# 순차 실행
import timeit
from urllib.request import urlopen

urls = [
    "https://google.com",
    "https://instagram.com",
    "https://tistory.com",
    "https://apple.com",
    "https://github.com",
]

start = timeit.default_timer()

# 순차 실행부
for url in urls:
    print("start", url)
    urlopen(url)
    print("end", url)

# 완료 시간 - 시작 시간
duration = timeit.default_timer() - start

print(duration)
