import re
p = input("Enter password: ")
if (re.search(r'[a-z]', p) and re.search(r'[A-Z]', p) and re.search(r'[0-9]', p) and re.search(r'[$#@]', p) and len(p) >= 6):
    print("Valid password")
else:
    print("Invalid password")
