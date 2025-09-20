# create a "Employee" class, and assign role, department, and salary
# create a "Engineer" class, and assign allthe attributes of Employee and assign two new attributes as name, and age

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def show_details(self):
        print(f"""
        ROLE        : {self.role}
        DEPARTMENT  : {self.department}
        SALARY      : {self.salary}
""")


class Engineer (Employee):
    def __init__(self, role, department, salary, name, age):
        super().__init__(role, department, salary)
        # super().__init__('Developer', 'tech', 53_000)         # or you can do this so that you can directly assign values to the parent
        self.name = name
        self.age = age

    def show(self):
        print(f"NAME        : {self.name}")
        print(f"AGE         : {self.age}")
        print(f"ROLE        : {self.role}")
        print(f"DEPARTMENT  : {self.department}")
        print(f"SALARY      : {self.salary}")



# ----------------------------------------------------------------------

e1 = Employee('Developer', 'tech', 53_000)

e1.show_details()

en1 = Engineer('Developer', 'tech', 53_000, 'Ravi Gupta', 25)
en1.show()
