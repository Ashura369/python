guests = ['amit','ravi','kishan', 'gopal']

# sending invitaion
for i in guests:
    print(f"Welcome Mr.{i.upper()}")

# suddenly amit cant come, so remove him and make a new invite for someone called shiva
guests.remove('ravi')
guests.insert(1, 'shiva')

print('*************************************************')
for i in guests:
    print(f"Welcome Mr.{i.upper()}")

