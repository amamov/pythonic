from pathlib import Path

# 현재 파일의 경로를 반환한다.
this_file_path = Path(__file__).resolve()
print(this_file_path)

# 현재 파일의 상위 폴더의 경로를 반환한다.
this_dir_path = this_file_path.parent
print(this_dir_path)