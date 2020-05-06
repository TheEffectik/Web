from math import factorial
pat = []
count = 0
for i in range(1, 25):
    b = factorial(25) / (factorial(i) * factorial(25 - i)) * (2 ** i)
    count += b
print(count % 243)