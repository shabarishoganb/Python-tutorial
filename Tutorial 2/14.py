import math
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)
n = int(input("Enter n: "))
r = int(input("Enter r: "))
print(factorial(n) // (factorial(r) * factorial(n - r)))
