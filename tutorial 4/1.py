class Arith:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def read(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))

    def add(self):
        return self.num1 + self.num2

arith = Arith()
arith.read()
print("Sum:", arith.add())
