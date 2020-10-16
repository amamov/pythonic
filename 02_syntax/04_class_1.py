#### class 1
# self, 클래스, 인스턴스

"""
클래스는 설계도이다. 클래스로 인스턴스화 시켜서 인스턴스(객체)를 만든다.
인스턴스들은 서로 독립적인 네임스페이스라는 창고를 이용해서 그 안에 값을 데이터를 저장한다.

클래스 : 객체를 만들기 위한 설계도 
인스턴스 : 클래스로 인스턴스화 하여 만든 대상 
객체 : 클래스를 기반으로 만들어진 실제 사물 (클래스의 인스턴스)

클래스 변수 : 클래스 내부에 선언된 변수, 객체보다 먼저 생성된다. 클래스 네임스페이스에 저장된다.
인스턴스 변수 : 객체마다 독립적으로 객체의 네임스페이스에 존재하고 인스턴스 생성 후 사용한다.
"""


class UserInfo:
    # 클래스 네임의 첫번째는 반드시 대문자로 하자!

    def __init__(self, name):
        # 인스턴스 변수
        self.name = name

    def user_info_print(self):
        # 메서드
        print("Name : ", self.name)


user1 = UserInfo("joy")  # 인스턴스
print(user1.name)
user1.user_info_print()

user2 = UserInfo("amamov")  # 인스턴스
print(user2.name)
user2.user_info_print()

print(id(user1))
print(id(user2))

print(user1.__dict__)  # user1 인스턴스 변수의 네임스페이스
# {'name': 'joy'}

print(user2.__dict__)  # user2 인스턴스 변수의 네임스페이스
# {'name': 'amamov'}


#### self의 이해 --> self는 인스턴스 객체이다!!
class SelfTest:
    # 클래스 변수
    name = "amamov"

    def function1():
        # 클래스 메서드
        print("function 1 called !")

    def function2(self):
        # 인스턴스 메서드
        print(id(self))  # 140514431978576
        print("function 2 called !")


test_instance = SelfTest()

# 클래스 변수는 클래스의 네임스페이스에 저장된다.
print(SelfTest.__dict__)  # {'name': 'amamov', ...}
print(test_instance.__dict__)  # {}

print(SelfTest.name)  # amamov
print(test_instance.name)  # amamov
# 인스턴스를 통해 변수에 접근하면 파이썬은 먼저 인스턴스의 네임스페이스에서 해당 변수가 존재하는지 찾는다.
# 해당 인스턴스의 네임스페이스에 해당 변수가 존재하지 않으면 클래스의 네임스페이스로 가서 다시 변수를 찾게 된다.

# self_instance.function1() # error
SelfTest.function1()  # 인스턴스에서는 호출 불가능
test_instance.function2()

print(id(test_instance))  # 140514431978576
