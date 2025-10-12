class Book:
    def __init__(self, title, pages):
        # __init__ → constructor
        self.title = title
        self.pages = pages

    def __str__(self):
        # __str__ → user-friendly string representation
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        # __len__ → allows using len() on object
        return self.pages

    def __add__(self, other):
        # __add__ → allows adding two books (total pages)
        return self.pages + other.pages


# creating objects
b1 = Book("Python Basics", 300)
b2 = Book("Data Science", 450)

# __str__
print(b1)     # Book: Python Basics, Pages: 300
print(b2)     # Book: Data Science, Pages: 450

# __len__
print(len(b1))   # 300

# __add__
print(b1 + b2)   # 750 (total pages when adding two books)      # if you remove the "__add__" method it will throw error
