from urllib import request
from urllib.error import URLError, HTTPError
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 다운로드 경로 및 파일명
save_path = {
    "image": str(BASE_DIR / "test_download_files" / "joy2.gif"),
    "html": str(BASE_DIR / "test_download_files" / "google.html"),
}

# 다운로드 테겟
target_url = {
    "image": "https://zmdzmd.net/wp-content/uploads/2020/03/%EC%A1%B0%EC%9D%B4-%EA%B0%80%EC%8A%B4-%EB%85%B8%EC%B6%9C.gif",
    "html": "https://www.google.co.kr/",
}

for target, url in target_url.items():
    try:
        # 웹 수신 정보 읽기
        response = request.urlopen(url)
        # 수신 내용
        contents = response.read()
        print("------------------------------------------------")
        print(f"Header Info - {target} : {response.info()}")
        print(f"HTTP Status Code - {target} : {response.getcode()}")
        with open(save_path[target], "wb") as file:
            file.write(contents)
    except HTTPError as error:
        print("Download failed.")
        print("HTTPError Code :", error.code)
    except URLError as error:
        print("Download failed.")
        print("URLError Code :", error.reason)
    else:
        print()
        print("Download Success!")
