from collections import Counter
nums = list(map(int, input("Enter numbers: ").split()))
mode = Counter(nums).most_common(1)[0][0]
print(mode)
