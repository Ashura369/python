# %% [markdown]
# # My First Notebook in VS Code
# This is a markdown cell. You can write notes here like in Jupyter.

# %%
# Import libraries
import numpy as np
import matplotlib.pyplot as plt

# %%
# Simple calculation
a = np.arange(1, 11)
b = a ** 2
print("Numbers:", a)
print("Squares:", b)

# %%
# Plot the results
plt.plot(a, b, marker="o")
plt.title("Numbers vs Squares")
plt.xlabel("Number")
plt.ylabel("Square")
plt.show()
