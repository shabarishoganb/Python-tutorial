class Student:
    def __init__(self):
        self.rollno = 0
        self.mark1 = 0
        self.mark2 = 0

    def readData(self, rollno, mark1, mark2):
        self.rollno = rollno
        self.mark1 = mark1
        self.mark2 = mark2

    def computeTotal(self):
        return self.mark1 + self.mark2

    def printDetails(self):
        print(f"Roll No: {self.rollno}, Marks: {self.mark1}, {self.mark2}, Total: {self.computeTotal()}")

student1 = Student()
student1.readData(101, 85, 90)
student1.printDetails()
