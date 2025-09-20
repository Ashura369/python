guests = ['amit','ravi','kishan', 'gopal', 'ramu', 'rohan']

# sending invitaion
for i in guests:
    print(f"Welcome Mr.{i.title()}")

# suddenly amit cant come, so remove him and make a new invite for someone called shiva
guests.remove('ravi')
guests.insert(1, 'shiva')

print('*************************************************')
for i in guests:
    print(f"Welcome Mr.{i.title()}")

print('*************************************************')

# you can only invite 2 ppl 
# Use pop() to remove guests from your list (from the last) one at a time until only two names remain in your list.

# only keep first 2 guests → remove the rest
while len(guests) > 2:
    removed = guests.pop(2)   # always remove the element at index 2 (third guest onward)
    print(f"Sorry Mr.{removed.title()}, you are no longer invited.")

print('*************************************************')
# final 2 invitations
for i in guests:
    print(f"Welcome Mr.{i.title()}")




