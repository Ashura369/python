# reverse of digits in a num

# 
num = 12345

a=0
while num > 0:
    digit = num % 10
    a = a*10+digit
    num = num // 10

print(a)













