y = int(input())
print("Leap year" if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else "Not leap year")
