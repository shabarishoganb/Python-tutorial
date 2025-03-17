while True:
    choice = int(input("1. Even/Odd\n2. Positive/Negative\n3. Factors\nEnter choice: "))
    num = int(input("Enter number: "))
    if choice == 1:
        print("Even" if num % 2 == 0 else "Odd")
    elif choice == 2:
        print("Positive" if num > 0 else "Negative" if num < 0 else "Zero")
    elif choice == 3:
        print([i for i in range(1, num + 1) if num % i == 0])
