## 하드 코딩
student_name_1 = "amamov"
student_number_1 = 3
student_grade_1 = 9
student_detail_1 = [
    {"gender": "Male"},
    {"score1": 99},
    {"score2": 100},
]

student_name_2 = "joy"
student_number_2 = 10
student_grade_2 = 1
student_detail_2 = [
    {"gender": "Female"},
    {"score1": 20},
    {"score2": 10},
]

student_name_3 = "yua"
student_number_3 = 4
student_grade_3 = 6
student_detail_3 = [
    {"gender": "Female"},
    {"score1": 50},
    {"score2": 100},
]

## 리스트를 사용하여 데이터 관리
student_name_list = ["amamov", "joy", "yua"]
student_number_list = [3, 10, 4]
student_grade_list = [9, 1, 6]
student_detail_list = [
    {"gender": "Male", "score1": 99, "score2": 100},
    {"gender": "Female", "score1": 20, "score2": 50},
    {"gender": "Female", "score1": 10, "score2": 100},
]

# 1번 학생 삭제
del student_name_list[1]
del student_number_list[1]
del student_grade_list[1]
del student_detail_list[1]

# 리스트 :  관리하기 불편하고 데이터의 정확한 위치(인덱스)를 매핑해서 사용해야 한다. 매우 매우 불편

## 딕셔너리를 사용하여 데이터 관리
students_dicts = [
    {
        "student_name": "amamov",
        "student_number": 3,
        "student_grade": 9,
        "student_detail": {"gender": "Male", "score1": 99, "score2": 100},
    },
    {
        "student_name": "joy",
        "student_number": 10,
        "student_grade": 1,
        "student_detail": {"gender": "Male", "score1": 20, "score2": 50},
    },
    {
        "student_name": "yua",
        "student_number": 4,
        "student_grade": 6,
        "student_detail": {"gender": "Male", "score1": 10, "score2": 100},
    },
]

# 1번 학생 삭제
del students_dicts[1]

# 딕셔너리 : 리스트보다 데이터 관리가 수월하지만 여전히 문제가 존재한다.


class Student:

    """ 클래스 기반 학생 데이터 : 재사용성 증가, 유지 보수 수월  """

    def __init__(self, name, number, grade, details):
        self.name = name
        self.number = number
        self.grade = grade
        self.details = details

    def __str__(self):
        return f"str : {self.name}"

    def __repr__(self):
        return f"str : {self.name}"


student1 = Student(
    name="amamov",
    number=10,
    grade=1,
    details={"gender": "Male", "score1": 99, "score2": 100},
)
student2 = Student(
    name="joy",
    number=10,
    grade=1,
    details={"gender": "Male", "score1": 20, "score2": 50},
)
student3 = Student(
    name="yua",
    number=4,
    grade=6,
    details={"gender": "Male", "score1": 10, "score2": 100},
)

print(student1)
print(student1.__dict__)  # namespace 확인
print(repr(student1))
