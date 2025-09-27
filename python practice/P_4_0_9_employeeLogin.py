# taking names as input
# print welcome message to everyone
emp = [
    "Amit", "Priya", "Rahul", "Sneha", "Vikram",
    "Anjali", "Rohit", "Pooja", "Karan", "Neha",
    "Suresh", "Divya", "Arjun", "Meera", "Varun",
    "Kavita", "Deepak", "Shreya", "Manoj", "Ritu"
]

admin = "shreya"
present = 3
attendence = []


for i in range(present):
    name = input(f"ENTER NAME : ")

    # greeting with good morning
    if name.lower() == admin.lower():
        print("HELLO ADMIN, WELCOME TO THE EXECUTIVE DESK")
    
    # Normal employee greeting
    elif name.lower() in [e.lower() for e in emp]:          # here we used elif bcoz, admin name is also on the list. And we wanted to avoid normal greeting for the admin. The elif function does this perfectly
        print("GOOD MORNING! WELCOME TO THE OFFICE")

    else:
        print("NAME NOT FOUND IN EMPLOYEE LIST")
    
    attendence.append(name)

absent = list(set(emp) - set(attendence))


print(f"TOTAL EMPLOYEE PRESENT {len(attendence)} \n\t {attendence}")
print(f"EMPLOYEE ABSENT ARE {len(absent)} \n\t {absent}")



