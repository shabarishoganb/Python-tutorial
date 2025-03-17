s = input("Enter string: ")
words = input("Enter words to remove: ").split()
for word in words:
    s = s.replace(word, "")
print(s)
