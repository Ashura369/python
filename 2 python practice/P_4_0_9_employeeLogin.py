# taking names as input
# print welcome message to everyone
# printing different messages for admins
# add working hours

emp = [
    "Amit", "Priya", "Rahul", "Sneha", "Vikram",
    "Anjali", "Rohit", "Pooja", "Karan", "Neha",
    "Suresh", "Divya", "Arjun", "Meera", "Varun",
    "Kavita", "Deepak", "Shreya", "Manoj", "Ritu"
]

admins = ["shreya", "Amit"]
present = 3     # change the number to increase or decrease the number of emps to be present
attendence = []


for i in range(present):
    name = input(f"ENTER NAME : ")

    # greeting with good morning
    if name.lower() in [a.lower() for a in admins]:
        print(f"HELLO!!!, WELCOME TO THE EXECUTIVE DESK {name.title()}\n")
    
    # Normal employee greeting
    elif name.lower() in [e.lower() for e in emp]:          # here we used elif bcoz, admin name is also on the list. And we wanted to avoid normal greeting for the admin. The elif function does this perfectly
        print(f"GOOD MORNING! WELCOME TO THE OFFICE {name.title()}\n")

    else:
        print(f"NAME {name} NOT FOUND IN EMPLOYEE LIST\n")
    
    attendence.append(name)

absent = list(set(emp) - set(attendence))

print()
print(f"TOTAL EMPLOYEE PRESENT {len(attendence)} \n\t {attendence}")
print(f"EMPLOYEE ABSENT ARE {len(absent)} \n\t {absent}")



