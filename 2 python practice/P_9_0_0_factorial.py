# factorial of a num using recursion

a = int(input("enter a number: "))

def facto(a):
    if a == 1:
        return 1

    ans = a * facto(a-1)
    return ans

print(f'the factorial of number {a} is {facto(a)}')
