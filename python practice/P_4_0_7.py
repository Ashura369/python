a = 3


if a<4:
    print('<4')
elif a<18:
    print('<18')
else:
    print('>18')
print('*'*50)
# ******************************************

if a<4:
    print('<4')
if a<18:
    print('<18')
else:
    print('>18')
print('*'*50)

# ******************************************

# when using elif it sometimes donot requre the else statement
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(price)
print('*'*50)

# ******************************************

# checking that a list is empty or not
letters = ['A','B','C','D','E']

nos = 0
if letters:     # checks wheather the list is empty or not
    for letters in letters:
        nos+=1
        print(f"item {nos} : {letters}")
else:
    print(f"THE LIST IS EMPTY")         # to print this statemetn just remove the items in the list

print('*'*50)
# ******************************************

# using multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping.title()} to your pizza")
    else:
        print(f"{requested_topping.title()} : OUT OF STOCK")

print('*'*50)
# ******************************************

menu = ['pizza', 'burger', 'chowmin', 'manchurian', 'coke', 'sprite', 'noodles', 'pasta']

print('MENU -->')

for num, item in enumerate(menu, start=1):     # "enumerate" is used when we want to print both the item and its index num, if you remove "start=1", the num will start from 0
    print(f"Item {num} : {item.title()}")


print()

food_ordered = []
total_items = int(input("HOW MANY ITEMS YOU WANT : "))
print(f"\nCHOOSE THE NUMBERS BETWEEN 1 TO {len(menu)} TO SELECT THE FOOD FROM THE MENU")

for i in range(total_items):
    a = int(input("ENTER THE FOOD NUMBER : "))
    food_ordered.append(a)

print(f"\nFOOD ORDERED --> ")
for i in food_ordered:
    print(f"{menu[i-1].title()}")       # here we did '-1' bcoz i start from 0






print('*'*50)