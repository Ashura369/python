# sum of digits in a num

num = 12345   # original number

# --- Using while loop ---
i = 0
temp = num    # make a copy so original num stays safe
while temp > 0:
    remainder = temp % 10
    i += remainder
    temp //= 10

print(i)   # 15
print('*'*120)


# --- Using for loop ---
a = 0
for el in str(num):    # now num is still 12345
    a += int(el)
print(a)   # 15
