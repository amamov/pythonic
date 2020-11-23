## 비동기 실행 (빅데이터 가져오기)
# concurrent.future 방법 2 (ProcessPoolExecutor)

# ThreadPoolExecutor의 GIL 문제를 우회한다. But CPU의 점유율이 엄청나다.

import time
import csv
from pathlib import Path
from concurrent import futures


# 추출할 국가 정보
NATION_LS = "Korea Italy Canada France Spain Maxico".split()

BASE_DIR = Path(__file__).resolve().parent

# 초기 데이터 csv 위치
TARGET_CSV = str(BASE_DIR / "resources" / "nations.csv")

# 추출한 데이터 저장 폴더 위치
SAVE_DIR = BASE_DIR / "csvs"

# CSV 헤더 기초 정보 가져오기
# with open(TARGET_CSV, "r") as file:
#     reader = csv.reader(file)
#     print(list(reader)[0])
HEADER = [
    "Region",
    "Country",
    "Item Type",
    "Sales Channel",
    "Order Priority",
    "Order Date",
    "Order ID",
    "Ship Date",
    "Units Sold",
    "Unit Price",
    "Unit Cost",
    "Total Revenue",
    "Total Cost",
    "Total Profit",
]


def save_csv(data, filename):
    save_path = str(SAVE_DIR / filename)
    with open(save_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADER)
        writer.writeheader()  # HEADER 쓰기
        for row in data:
            writer.writerow(row)


# 데이터 추출
def get_sales_data(nation):
    with open(TARGET_CSV, "r") as file:
        reader = csv.DictReader(file)
        data = []
        for r in reader:
            # 조건에 맞는 국가만 출력
            if r["Country"] == nation:
                data.append(r)
        # print(data)
    return data


# 국가별 분리 함수
def seperate_many(nation):
    # 데이터를 분리
    data = get_sales_data(nation)
    # 파일 저장
    save_csv(data=data, filename=nation.lower() + ".csv")
    return nation


# 시간 측정 및 main 함수
def main(seperate_many):
    # 시작시간
    start_time = time.time()
    # worker 개수 (일꾼 수)
    worker = min(20, len(NATION_LS))  # 둘 중에 작은 값을 꺼내준다. 즉, worker = 6
    # 결과 건수
    with futures.ProcessPoolExecutor(max_workers=worker) as executor:
        result_cnt = executor.map(seperate_many, NATION_LS)

    # 종료시간
    end_time = time.time()

    print(f"{result_cnt} : {end_time - start_time}")


if __name__ == "__main__":
    main(seperate_many)