from urllib import request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 파일 url
img_url = "https://zmdzmd.net/wp-content/uploads/2020/03/%EC%A1%B0%EC%9D%B4-%EA%B0%80%EC%8A%B4-%EB%85%B8%EC%B6%9C.gif"
html_url = "https://www.google.co.kr/"

# 다운받을 경로
save_img_path = str(BASE_DIR / "test_download_files" / "joy.gif")
save_html_path = str(BASE_DIR / "test_download_files" / "index.html")

try:
    img_file, img_header = request.urlretrieve(img_url, save_img_path)
    html_file, html_header = request.urlretrieve(img_url, save_html_path)
except Exception as error:
    print("Download Fail")
    print(error)
else:
    # http는 1회성 연결이다. 요청을 하고 응답을 하면 연결이 끊긴다.
    print()
    print("image header > ", img_header)
    print("html header > ", html_header)

    # 다운로드 파일 정보
    print()
    print(f"Filename : {img_file}")
    print(f"Filename : {html_file}")

    print()
    print("Download Success")
