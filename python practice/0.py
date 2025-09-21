# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
# 2x2 matrix
matrix = np.array([[1, 3],
                   [2, 4]])

# Take each row as (x, y) points
x = matrix[:, 0]  # first column
y = matrix[:, 1]  # second column

# %%
# Plot the points and connect with a line
plt.plot(x, y, marker='o', linestyle='-', color='blue', label='2x2 points')
plt.title("2x2 Matrix Graph")
plt.xlabel("First column")
plt.ylabel("Second column")
plt.grid(True)
plt.legend()
plt.show()
