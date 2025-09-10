a = [1,3,84,56,4,42,57,1,58,4212,1845,154,84,54,84,1,48,45,151,584,51,5,484,21,54,5]

print('-' * 120)

# sort + remove duplicates in one line
a = sorted(set(a))
print(a)

print('-' * 120)
# --------------------------------------------------------------------------------------


# printing using for loop and idx
for idx, i in enumerate(a):
    if idx == len(a) - 1:
        print(i)
    else:
        print(i, '--', end=" ")

print('-' * 120)
# --------------------------------------------------------------------------------------

# printing using slicing
for i in a[:-1]:
    print(i, '-->', end=' ')
print(a[-1])  # last element without "-->"

print('-' * 120)
# --------------------------------------------------------------------------------------

# sorting in descending order
a = sorted(a, reverse=True)
print(a)
print('-' * 120)
# --------------------------------------------------------------------------------------



