# a block of statements that perform a specific task

def sum(a, b):
    s = a + b
    return s


def minus(a, b):
    if a > b:
        n = a-b
    elif b > a:
        n = b-a

    return n

print(sum(2, 5))
print(minus(7,5))

print('*'*120)

ans = sum(2,5) * minus(7,5)
print(ans)

print('*'*120)
# **************************************************************************************************


def pr():
    print('hii')

def pr():
    print('hoo')


pr()    # will print 'hoo', bcoz we overwrite the value
print('*'*120)

print('*'*120)
# **************************************************************************************************


def r1(a=1, b=1):
    print(a*b)

r1()    # even if you dont put any arguments while calling r1, it will take 1 as auguments in the function 

r1(3)   # if you want assign only one value then only the first value will be assigned, you cant assign values to the second parameter


