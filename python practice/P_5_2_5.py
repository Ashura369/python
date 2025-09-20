# making a list by taking input

list = []

n = int(input("ENTER THE NUMBER OF WORDS YOU WANT TO ENTER IN THE LIST: "))

for i in range(n):
    enter = input(f"ENTER WORD {i+1}: ")
    list.append(enter)

print(list)







    