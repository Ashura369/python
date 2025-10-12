# Taking different types of input in Python

# String input
name = input("Enter your name: ")
print("Name:", name, "| Type:", type(name))

# Integer input
age = int(input("Enter your age: "))
print("Age:", age, "| Type:", type(age))

# Float input
height = float(input("Enter your height in meters: "))
print("Height:", height, "| Type:", type(height))

# Boolean input (True/False)
is_student = input("Are you a student? (yes/no): ").strip().lower() == "yes"
print("Is Student:", is_student, "| Type:", type(is_student))

# List input (comma-separated values)
numbers = list(map(int, input("Enter numbers separated by commas: ").split(",")))
print("Numbers:", numbers, "| Type:", type(numbers))

