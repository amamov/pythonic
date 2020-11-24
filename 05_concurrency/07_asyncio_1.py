"""
asyncio(Asynchronous I/O)는 비동기 프로그래밍을 위한 모듈이며 CPU 작업과 I/O를 병렬로 처리하게 해준다.

"""

# 순차 실행
from time import time
from urllib.request import urlopen

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

# 순차 실행부
for url in urls:
    print("start", url)
    urlopen(url)
    print("end", url)

# 완료 시간 - 시작 시간
duration = time() - start

print(duration)
