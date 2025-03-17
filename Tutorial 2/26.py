    nums = list(map(int, input("Enter numbers: ").split()))
primes = [n for n in nums if all(n % i != 0 for i in range(2, int(n**0.5) + 1)) and n > 1]
composites = [n for n in nums if n not in primes and n > 1]
print("Primes:", primes, "Composites:", composites)
