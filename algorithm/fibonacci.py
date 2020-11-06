def fibonacci(size_of_fibonacci: int) -> list:
    first, second = 0, 1
    fibonacci_seq = [first, second]
    for _ in range(size_of_fibonacci - 2):
        first, second = second, first + second
        fibonacci_seq.append(second)
    return fibonacci_seq


if __name__ == "__main__":
    fibo = fibonacci(15)
    print(fibo)

# 피보나치와 치킨
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
# 3명일때 2마리, 5명일때 3마리, 8명일때 5마리 13명일때 8마리...
# 30명일때 몇마리? -> 34 : 21 = 30 : x -> x마리!
