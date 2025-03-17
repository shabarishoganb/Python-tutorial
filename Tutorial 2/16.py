import math
x = float(input("Enter x: "))
n = int(input("Enter n: "))
sin_x = sum(((-1)**i * (x**(2*i+1)) / math.factorial(2*i+1)) for i in range(n))
print("sin(x) =", sin_x)
