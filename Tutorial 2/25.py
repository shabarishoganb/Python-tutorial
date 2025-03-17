data = input("Enter data: ").split()
ints, floats, strings = [], [], []
for d in data:
    if d.isdigit():
        ints.append(int(d))
    elif "." in d:
        floats.append(float(d))
    else:
        strings.append(d)
print("Ints:", ints, "Floats:", floats, "Strings:", strings)
