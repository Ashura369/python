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



