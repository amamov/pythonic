import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SAVE_PATH = str(BASE_DIR / "test_make_folder")

try:
    # 폴더가 이미 존재하는지 체크
    if not (os.path.isdir(SAVE_PATH)):
        # 없으면 폴더 생성
        os.makedirs(SAVE_PATH)
except OSError as error:
    print("Folder creation failed.")
    print(f"Folder name : {error.filename}")
    raise RuntimeError("System Exit!")
else:
    # 이미 폴더가 존재할 경우
    print("Folder is created!")
