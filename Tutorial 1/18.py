n = int(input())
print("Armstrong" if sum(int(d)**len(str(n)) for d in str(n)) == n else "Not Armstrong")
