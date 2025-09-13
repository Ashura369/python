a = ["zebra", "apple", "mango", "kite", "banana", "grape", "dog", "elephant", "cat", "fish", "xylophone", "orange", "lion", "tiger", "bear"]

def order(a, idx=0):
    if idx == len(a)-1:
        return a
    
    for i in range(len(a)-1-idx):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    
    return order(a, idx+1)


print(order(a))

