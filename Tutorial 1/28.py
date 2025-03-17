l, u = int(input()), int(input())
print(sum(x for x in range(l, u+1) if x % 2 == 1))
