list = ['hii', 'alpha', 'apple', 'dog', 'cat', 'cooper']
print(len(list))
def order(list, n=None):
    if n is None:
        n = len(list)
    
    # base case
    if n == 1:
        return list
    
    for i in range(n-1):
        if list[i] > list[i+1]:
            # swap
            list[i], list[i+1] = list[i+1], list[i]

            '''
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
            
            '''
    
    # recursive call for the remaining part
    return order(list, n-1)

print(order(list))

'''OTHER WAY TO SOLVE THE PROBLEM'''

list = ["zebra", "apple", "mango", "kite", "banana", "grape", "dog", "elephant", "cat", "fish", "xylophone", "orange", "lion", "tiger", "bear"]

def order2(a, idx=0):
    if idx == len(list)-1:
        return list

    for i in range(len(list)-1-idx):

        if list[i] > list[idx]:
            list[i], list[i+1] = list[i+1], list[i]
    
    return order2(a, idx+1)


print(order2(list))

