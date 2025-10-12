# findig the sum of first N natural numbers

def sum(a):

    if a == 1:
        return 1

    ans = a + sum(a-1)
    return ans

print(sum(5))



