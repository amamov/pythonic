# Block I/O : 한 요청을 할때 모든 스레드가 멈춰있는 것이다. 즉, 한 명이 일을 끝내지 않으면 일을 할 수 없는 상태(순차 실행)
# 멀티 스레드로 구현 (GIL 문제 염두)
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading  # 스레드 이름을 출력하기 위해

urls = [
    "https://google.com",
    "https://instagram.com",
    "https://tistory.com",
    "https://apple.com",
    "https://github.com",
]

start = timeit.default_timer()


def fetch(url):
    print("Thread Name : ", threading.current_thread().getName(), "start", url)
    urlopen(url)
    print("Thread Name : ", threading.current_thread().getName(), "done", url)


def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in urls:
            executor.submit(fetch, url)


if __name__ == "__main__":
    main()
    # 완료 시간 - 시작 시간
    duration = timeit.default_timer() - start
    print(duration)
