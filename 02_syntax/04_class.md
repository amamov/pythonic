# class

1. 클래스와 인스턴스
2. self의 이해
3. 상속
4. 오버라이딩 & super()
5. 다중상속

---

### Intro

- 클래스 : 객체를 만들기 위한 설계도
- 인스턴스 : 클래스로 인스턴스화 하여 만든 대상 (객체)
- 객체 : 클래스를 기반으로 만들어진 실제 사물 (클래스의 인스턴스)
- 클래스 변수 : 클래스 내부에 선언된 변수, 인스턴스보다 먼저 생성된다. 클래스 네임스페이스에 저장된다.
- 인스턴스 변수 : 인스턴스마다 독립적으로 인스턴스의 네임스페이스에 존재하고 인스턴스 생성 후 사용한다.
- 클래스로 인스턴스화 시켜서 인스턴스(객체)를 만든다. 인스턴스들은 서로 독립적인 네임스페이스라는 창고를 이용해서 그 안에 값을 저장한다.
  <br />
- [관련 함수]

```
MyClass.__dict__ --> 클래스의 내임스페이스를 보여준다.
MyClass.mro() --> 클래스의 상속관계를 보여준다.
```

**이건뭐지**

---

### What is the 'namespace' ?

네임스페이스(namespace, 이름공간)란 프로그래밍 언어에서 특정한 객체(Object)를 이름(Name)에 따라 구분할 수 있는 범위를 의미한다. 파이썬 내부의 모든것은 객체로 구성되며 이들 각각은 특정 이름과의 매핑 관계를 갖게 되는데 이 매핑을 포함하고 있는 공간을 네임스페이스라고 한다.

### How Use ?

- 클래스 선언

```
class UserInfo:

    ## 초기화
    def __init__(self, name):
        ## 인스턴스 변수
        self.name = name

    ## 인스턴스 메서드
    def user_info_print(self):
        print("Name : ", self.name)
```

- 인스턴스 생성 & 인스턴스 변수를 네임스페이스에 저장

```
user1 = UserInfo("joy")

user2 = UserInfo("amamov")
```

- 인스턴스 네임스페이스에서 인스턴스 변수를 꺼낸다.

```
print(user1.name)
# joy

print(user2.name)
# amamov
```

- 인스턴스 메서드 호출

```
user1.user_info_print()
# Name :  joy

user2.user_info_print()
# Name :  amamov
```

- 하나의 클래스에서 생성된 각각의 인스턴스들은 서로 독립적이다.

```
print(id(user1))
# 140424922290960

print(id(user2))
# 140424922290960
```

- 인스턴스의 네임스페이스 확인

```
print(user1.__dict__)
# {'name': 'joy'} --> user1의 네임스페이스

print(user2.__dict__)
# {'name': 'amamov'} --> user2의 네임스페이스
```

---

### self의 이해 --> self는 인스턴스 객체이다!!

```
class SelfTest:

    ## 클래스 변수
    name = "amamov"

    ## 클래스 메서드
    def function1():
        print("function 1 called !")

    ## 인스턴스 메서드
    def function2(self):
        print("function 2 called !")

        print(id(self))
        # 140514431978576

test_instance = SelfTest()
```

- 클래스 변수는 클래스의 네임스페이스에 저장된다.

```
## 클래스의 네임스페이스
print(SelfTest.__dict__)
# {'__module__': '__main__', 'name': 'amamov', 'function1': <function SelfTest.function1 at 0x7ff841bc95f0>, 'function2': <function SelfTest.function2 at 0x7ff841bc9680>, '__dict__': <attribute '__dict__' of 'SelfTest' objects>, '__weakref__': <attribute '__weakref__' of 'SelfTest' objects>, '__doc__': None}
```

```
## 인스턴스의 네임스페이스
print(test_instance.__dict__)
# {}
```

- 인스턴스를 통해 변수에 접근하면 파이썬은 먼저 인스턴스의 네임스페이스에서 해당 변수가 존재하는지 찾는다. 해당 변수가 네임스페이스에 존재하지 않으면 클래스의 네임스페이스로 가서 다시 변수를 찾게 된다.

```
## name : 클래스 변수
print(SelfTest.name)
# amamov

print(test_instance.name)
# amamov
```

- 클레스 메서드는 인스턴스에서 호출 불가능

```
self_instance.function1() # error

SelfTest.function1()
# function 1 called !

test_instance.function2()
# function 2 called !
```

- 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다! 즉, self는 인스턴스 그 자체이다!

```
print(id(test_instance))  # 140514431978576
```

---

### 상속

- Super 클래스를 Sub 클래스가 상속받았을 때 Super 클래스를 부모 클래스(슈퍼 클래스)라고 하고 Sub 클래스를 자식 클래스(서브 클래스)라고 정의한다.
- 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에도 담긴다.
- 자식 클래스에는 별도의 메서드를 추가할 수 있다.
- 관련 함수 : MyClass.mro() --> 상속 관계를 보여준다.

```
class Mother:
    age = 23

    def __init__(self, color):
        self.color = color

    def run(self):
        print("달리는 능력")


## Son 클래스가 Mother 클래스를 상속받았다.
class Son(Mother):
    def jump(self):
        print("점프하는 능력")
        print("상속 받은 인스턴스 변수 : ", self.color)

        ## 클래스 변수는 인스턴스의 네임스페이스에는 존재하지 않는다.
        print("상속 받은 클래스 변수 : ", self.age)


son1 = Son("white")

print(son1.age)
# 23 (상속)

print(son1.color)
# white (상속)

son1.run()
# 달리는 능력 (상속)

son1.jump()
# 점프하는 능력

```

---

### 메서드 오버라이딩

- 부모 클래스가 갖는 메서드와 동일한 이름의 메서드를 자식 클래스가 정의하는 경우를 메서드 오버라이딩이라고 한다. 이 경우 부모 클래스의 메서드는 호출이 불가능한 상태가 된다.

```

class Mother:
    def run(self):
        print("달리는 능력")


class Son(Mother):
    ## 오버라이딩
    def run(self):
        print("아들만의 달리는 능력")


son1 = Son()

son1.run()
# 아들만의 달리는 능력 (오버라이딩)

```

---

### super()

- super()을 사용하여 부모 클래스의 메서드를 가져올 수 있다.

```
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

```

---

### 다중상속

- 파이썬의 모든 것들은 object에 상속받는다.

```
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
```
