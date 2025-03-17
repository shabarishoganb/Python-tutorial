nums = [int(input()) for _ in range(int(input()))]
print(sum(x % 2 == 0 for x in nums), sum(x % 2 == 1 for x in nums))
