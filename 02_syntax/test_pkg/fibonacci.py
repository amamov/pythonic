class Fibonacci:
    def __init__(self, title="fibonacci"):
        self.title = title

    def fib_num(self, number: int) -> int:
        first, second = 0, 1
        while first < number:
            first, second = second, first + second
        return first

    def fib_list(self, number: int) -> list:
        result = []
        first, second = 0, 1
        while first < number:
            result.append(first)
            first, second = second, first + second
        return result


if __name__ == "__main__":
    # 단위 테스트할 때 사용한다. 이 식의 의미는 현재 이 파일이 메인으로 사용될때만 실행한다.
    pass
