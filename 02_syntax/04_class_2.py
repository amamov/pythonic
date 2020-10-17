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
        return f'Car Class "Show color ! {self.color}"'


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
# red

print(model1.car_type)  # Super
# sedan

print(model1.car_name)  # Sub
# sexy

print(model1.show())  # Super
# Car Class "Show color ! red"

print(model1.show_model())  # Sub
# Your Car Name : sexy

print(model1.__dict__)
# {'car_type': 'sedan', 'color': 'red', 'car_name': 'sexy'}


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
# 오버라이딩 오버라이딩!!

## 다중상속
print(BMW.mro())  # 상속 관계를 보여준다.
# [<class '__main__.BMW'>, <class '__main__.Car'>, <class 'object'>]
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
# [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]


class Mother:
    def run(self):
        print("달리는 능력")


class Son(Mother):
    def jump(self):
        print("점프하는 능력")

    ## 오버라이딩
    def run(self):
        print("아들만의 달리는 능력")

    ## super()
    def mother_run(self):
        super().run()

        print(super())
        # <super: <class 'Son'>, <Son object>>

        print(type(super()))
        # <class 'super'>


son1 = Son()

son1.run()
# 아들만의 달리는 능력 (오버라이딩)

son1.mother_run()
# 달리는 능력 (super()을 이용한 부모클래스의 메서드 사용)

son1.jump()
# 점프하는 능력
