# [Exceptions] 예외 처리

- 최대한 예외가 발생하지 않을 것으로 가정하고 먼저 코딩하고 그 후 런타임 예외 발생시 예외 처리를 권장 (EAEP 코딩 스타일)

1. 문법적 에러
2. 런타임 에러 (코드 실행(런타임)프로세스에서 발생하는 예외)
3. Try-except-else-finally

- linter : 코드 스타일, 문법 에러를 감지한다.

### 대표적인 에러 정리

<!-- https://python.bakyeono.net/chapter-9-4.html -->

1. SyntaxError : 문법 에러

```
print('Error)
# SyntaxError: EOL while scanning string literal
```

2. NameError : 참조 변수가 없을 떄 발생

```
a = 10
print(b)
# NameError: name 'b' is not defined
```

3. ValueError : 참조 값이 없을때 발생

```
x = [1, 5, 9]
x.remove(10)
# ValueError: list.remove(x): x not in list
```

4. TypeError

```
x = [1, 2]
y = "test"
print(x + y)
# TypeError: can only concatenate list (not "str") to list
```

5. IndexError : 인덱스 범위 오버

```
x = [1, 2, 3]
print(x[10])
# IndexError: list index out of range
```

6. ZeroDivisionError: division by zero (런타임 에러)

```
print(10 / 0)
```

7. KeyError

```
my_dict = {"name": "amamov", "age": 23}
print(my_dict["hobby"])
# KeyError: 'hobby'
```

8. AttributeError : 존재하지 않는 속성에 접근하였을 때 발생한다.

```
import time

print(time.nothing())
# AttributeError: module 'time' has no attribute 'nothing'
```

8. FileNotFoundError : 해당하는 파일이 없을 때 에러가 발생한다.

```
file = open("nothing.txt", "r")
# FileNotFoundError: [Errno 2] No such file or directory: 'nothing.txt'
```

### Try-except-else-finally

1. try : 에러가 발생할 가능성이 있는 코드 실행
2. except : 에러명 1
3. except : 에러명 2
4. else : 에러가 발생하지 않았을 경우 실행
5. finally : 예외 발생 여부와 관계 없이 항상 실행

- 예외 처리 기본

```
my_list = [1, 2, 3]

try:
    x = my_list.index(4)
    print(f"{x} is in list!")
except ValueError:
    print("Not Found id! - ValueError !")
else:
    print("Ok else !")

# Not Found id! - ValueError !
```

- 어떤 에러가 발생할지 모르면 Exception을 사용한다. except: 만으로도 사용 가능하다.

```
try:
    x = my_list.index(4)
    print(f"{x} is in list!")
except Exception:
    print("Not Found id! - Error !")
else:
    print("Ok else !")

# Not Found id! - Error !
```

- finally는 예외 발생 여부와 관계 없이 항상 발생한다.

```
try:
    x = my_list.index(4)
    print(f"{x} is in list!")
except:
    print("Not Found id! - Error !")
else:
    print("Ok else !")
finally:
    print("Finally !")

# Not Found id! - Error !
# Finally !
```

- as를 이용하여 에러 메세지를 출력할 수 있다.

```
try:
    x = my_list.index(4)
    print(f"{x} is in list!")
except ValueError as error_message:
    print(error_message)
except IndexError:
    print("Ok else !")
except Exception:
    print("Error")
finally:
    print("Finally !")

# 4 is not in list
# Finally !
```

- raise를 사용하여 에러를 직접 발생시킬 수 있다.

```
try:
    a = "Yoon"
    if a == "yoon":
        print("Okay !")
    else:
        raise ValueError
except ValueError:
    print("Value Error!")
except Exception:
    print("Error!")
else:
    print("OK")

# Value Error!
```

-
