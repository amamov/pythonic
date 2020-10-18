n = int(input("Enter the number : "))

if n % 2 == 0 and n % 3 == 0:
    print(n, " is divisible by 2 and 3.")
elif n % 2 == 0 or n % 3 == 0:
    print(n, " is divisible by 2 or 3.")
elif (n % 2 == 0 or n % 3 == 0) and not (n % 2 == 0 and n % 3 == 0):
    print(n, " is divisible by 2 or 3, but not both.")
else:
    print("wow !")


# Enter the number : 3
# 3  is divisible by 2 or 3.
