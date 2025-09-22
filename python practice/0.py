import numpy as np


a = np.array([1, 2, 3, 4, 5])            # 1D array from list
b = np.arange(0, 10, 2)                   # 0 to 9 with step 2
c = np.zeros((2, 3))                      # 2x3 array of zeros
d = np.ones((3, 2))                       # 3x2 array of ones
e = np.eye(3)                             # 3x3 identity matrix
f = np.linspace(0, 1, 5)                  # 5 points evenly spaced between 0 and 1
g = np.random.rand(2, 2)                  # 2x2 random numbers between 0 and 1
h = np.random.randint(0, 10, size=(3, 3)) # 3x3 random integers from 0 to 9

print("a:", a)
print("b:", b)
print("c:\n", c)
print("d:\n", d)
print("e:\n", e)
print("f:", f)
print("g:\n", g)
print("h:\n", h)