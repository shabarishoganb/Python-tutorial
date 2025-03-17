nums = list(map(int, input("Enter numbers: ").split()))
unique = [n for n in nums if nums.count(n) == 1]
print(unique)
