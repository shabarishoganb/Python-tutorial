a, b, c = float(input()), float(input()), float(input())
d = b**2 - 4*a*c
print("No real roots" if d < 0 else (-b + d**0.5) / (2*a), (-b - d**0.5) / (2*a))
