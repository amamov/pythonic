def combination(n, r):
    result = 1
    for i in range(1, r + 1):
        result *= (n - (r - i)) / (r - (r - i))
    return int(result)


if __name__ == "__main__":
    print("[nCr]")
    n = int(input("Input the n: "))
    r = int(input("Input the r: "))
    result = combination(n, r)
    print(result)
