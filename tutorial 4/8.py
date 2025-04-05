class Book:
    def __init__(self):
        self.title = ""
        self.author = ""
        self.cost = 0

    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def print_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Cost: {self.cost}")

book1 = Book()
book1.get_details("Python Programming", "Guido van Rossum", 50)
book1.print_details()
