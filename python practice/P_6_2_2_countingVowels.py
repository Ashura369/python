# Counting vowels in a string

a = input("ENTER THE STRING: ")
vowels = "aeiouAEIOU"
count = 0

for char in a:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
