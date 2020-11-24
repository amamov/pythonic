# Block I/O : 한 요청을 할때 모든 스레드가 멈춰있는 것이다. 즉, 한 명이 일을 끝내지 않으면 일을 할 수 없는 상태(순차 실행)
# 단일 스레드의 asyncio로 병령처리

# aiohttp (asyncio 지원) pipenv install aiohttp
from time import time
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import asyncio

urls = [
    "https://google.com",
    "https://instagram.com",
    "https://tistory.com",
    "https://apple.com",
    "https://github.com",
    "https://google.com",
    "https://instagram.com",
    "https://tistory.com",
    "https://apple.com",
    "https://github.com",
]

start = time()


async def fetch(url, executor):
    # object HTTPResponse can't be used in 'await' expression await 뒤에는 async 함수가 와야한다.
    # response = await urlopen(url)
    response = await loop.run_in_executor(
        executor, urlopen, url
    )  # 일꾼(executor) 한명 당 urlopen 함수에 url을 넣어서 실행
    return response.read()


async def main():
    # 스레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    futures = [asyncio.ensure_future(fetch(url, executor)) for url in urls]
    result = await asyncio.gather(*futures)  # Promise.all([]) 같은 개념
    print(result)


if __name__ == "__main__":
    # 루프 생성
    loop = asyncio.get_event_loop()  # 중앙에서 관리하도록 한다.
    # 루프 대기
    loop.run_until_complete(main())  # main()이 완료될 때까지 기다린다.

    main()
    # 완료 시간 - 시작 시간
    duration = time() - start
    print(duration)
