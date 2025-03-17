s = input("Enter a string: ")
vowels = "aeiouAEIOU"
print("".join([ch for ch in s if ch not in vowels]))
