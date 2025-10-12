x = 10
y = 20

if x > y:
    print("x is greater")
elif x < y:
    print("y is greater")
else:
    print("x and y are equal")

print("************************************")

a, b = 25, 220
print("a is greater" if a > b else "b is greater" if a < b else "a and b are equal")

print("************************************")

height = 5.7
weight = 58

if height is not None and weight is not None:
    print("height -", height, "weight -", weight)
else:
    print("values are missing")    

# "null" is not valid in py, you have to write "None" 