s = input("Enter a string: ")
mid = len(s) // 2
print(s[:mid][::-1] + s[mid:][::-1])
