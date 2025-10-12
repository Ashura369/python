# finding factorial of a num using function

def facto(a):
    ans=1
    for i in range(a, 0, -1):
        ans *= i
    print(f'factorial of num {a} is : ',ans)


facto(5)
facto(8)





