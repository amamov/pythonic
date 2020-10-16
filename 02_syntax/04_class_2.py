#### class 2
## 상속, 오버라이딩, 다중상속

"""
슈퍼클래스(부모) 및 서브클래스(자식) --> 모든 속성, 메서드 사용 가능
.mro() --> 상속 관계를 보여준다.
"""


class Car:
    """ Super Class """

    def __init__(self, car_type, color):
        self.car_type = car_type
        self.color = color

    def show(self):
        return 'Car Class "Show Method !"'


## 상속
class BMW(Car):
    """ Sub Class """

    def __init__(self, car_name, car_type, color):
        super().__init__(car_type, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return f"Your Car Name : {self.car_name}"


model1 = BMW("sexy", "sedan", "red")  # 인스턴스 생성

# 슈퍼 클래스의 모든 속성, 메서드 사용 가능
print(model1.color)  # Super
print(model1.car_type)  # Super
print(model1.car_name)  # Sub
print(model1.show())  # Super
print(model1.show_model())  # Sub

print(model1.__dict__)


## 메서드 오버라이딩
class Benz(Car):
    """ Sub Class """

    def __init__(self, car_name, car_type, color):
        super().__init__(car_type, color)
        self.car_name = car_name

    def show_model(self) -> None:
        return f"Your Car Name : {self.car_name}"

    def show(self):
        # 슈퍼클래스의 show 메서드를 오버라이딩하였다.
        return "오버라이딩 오버라이딩!!"


model2 = Benz("밴찌 2", "wow", "blue")  # 인스턴스 생성

print(model2.show())  # 오버라이딩

## 다중상속
print(BMW.mro())  # 상속 관계를 보여준다.
# 파이썬의 모든 것들은 object에 상속받는다.


class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


print(M.mro())