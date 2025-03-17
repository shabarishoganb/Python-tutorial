s = input("Enter a string: ")
is_palindrome = all(s[i] == s[-(i + 1)] for i in range(len(s) // 2))
print("Palindrome" if is_palindrome else "Not a palindrome")
