# sum from n=1 to n=infinity, 1/n^2 --> pi^2/6, Find c ; pi^2/c
from math import pi

total = 0
infinity = 99999
for i in range(1, infinity):
    total += 1 / (i ** 2)

c = pi ** 2 / total

print("%.4f" % (c))
