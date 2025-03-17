def fact(n):
    return 1 if n == 0 else n * fact(n - 1)
n = int(input("Enter number: "))
print(fact(n))
