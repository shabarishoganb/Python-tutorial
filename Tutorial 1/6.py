a, b, c = sorted([int(input()) for _ in range(3)])
print("Right-angled" if a**2 + b**2 == c**2 else "Not right-angled")
