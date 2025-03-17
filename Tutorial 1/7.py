x, y = int(input()), int(input())
print("Quadrant 1" if x > 0 and y > 0 else "Quadrant 2" if x < 0 and y > 0 else "Quadrant 3" if x < 0 and y < 0 else "Quadrant 4" if x > 0 and y < 0 else "On axis")
