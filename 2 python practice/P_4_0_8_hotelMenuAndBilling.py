# MAKING A HOTEL MENU WITH FINAL BILLING
menu = ['pizza', 'burger', 'chowmin', 'manchurian', 'coke', 'sprite', 'noodles', 'pasta', 'sandwich', 'french fries', 'momos', 'biryani', 'coffee', 'ice cream', 'salad']

price = [150, 80, 50, 60, 20, 20, 70, 120, 60, 40, 80, 200, 50, 90, 70]

# showing menu to the customer
print('MENU -->')
for num, item in enumerate(menu, start=1):     # "enumerate" is used when we want to print both the item and its index num, if you remove "start=1", the num will start from 0
    print(f"Item {num} : {item.title()}")


print()

# taking order from the customer
food_ordered = []
food_plates = []
total_items = int(input("HOW MANY ITEMS YOU WANT : "))
print(f"\nCHOOSE THE NUMBERS BETWEEN 1 TO {len(menu)} TO SELECT THE FOOD FROM THE MENU")

for idx, _ in enumerate(range(total_items), start=1):
    a = int(input("ENTER THE FOOD NUMBER : "))
    b = int(input(f"\tHOW MANY UNITS YOU WANT OF FOOD {menu[a-1].title()} (RS.{price[a-1]} EACH) : "))
    food_ordered.append(a-1)
    food_plates.append(b)
    

# showing the list of food he has ordered
print(f"\nFOOD ORDERED --> ")
print(f"ORDER FOR : ", end=" ")
totalPrice = 0
for idx, (i,j) in enumerate(zip(food_ordered, food_plates), start=1):
    if idx < len(food_ordered):
        print(f"\n{j} {menu[i]} : RS. {price[i]*j} ({price[i]} each)", end=", ")       # here we did '-1' bcoz i start from 0
        totalPrice += price[i]*j
    else:
        totalPrice += price[i]*j
        print(f"\n{j} {menu[i]} : RS. {price[i]*j} ({price[i]} each)", end=" ")
        print(f"\nTOTAL BILL : {totalPrice}")
        

# others method to do the same
"""
    for i, j in zip(food_ordered, food_plates):
        print(f"{j} {menu[i]}", end=", ")       # here we did '-1' bcoz i start from 0
"""

""" 
    orders = [f"{j} {menu[i-1].title()}" for i, j in zip(food_ordered, food_plates)]
    print(", ".join(orders))
"""

