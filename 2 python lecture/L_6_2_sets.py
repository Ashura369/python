# set is the collection of unordered items
# each element must be unique and immutable
    # it means set itself is mutable but the elements in the set are mutable

# SETS IN PYTHON

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Sets automatically remove duplicates
duplicate_set = {1, 2, 2, 3, 4, 4, 5}
print("Set with duplicates removed:", duplicate_set)

print("*********************************************")

# Adding elements
my_set.add(6)   # can only add one element at a time
print("After adding 6:", my_set)

# Adding multiple elements
my_set.update([7, 8, 9])
print("After updating with [7, 8, 9]:", my_set)

print("*********************************************")

# Removing elements
my_set.remove(3)  # Throws error if element not found
print("After removing 3:", my_set)

my_set.discard(10)  # Doesn't throw error if element not found
print("After discarding 10 (non-existent):", my_set)

print("*********************************************")

# Using pop (removes a random element)
popped_element = my_set.pop()
print("Element popped from my_set:", popped_element)
print("Set after pop:", my_set)

print("*********************************************")

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Set A:", a)
print("Set B:", b)
print()

# Union
print("Union (a | b):", a | b)
print("Union using method:", a.union(b))
print()

# Intersection
print("Intersection (a & b):", a & b)
print("Intersection using method:", a.intersection(b))
print()

# Difference
print("Difference (a - b):", a - b)  # removes common elements of b from a
print("Difference using method:", a.difference(b))
print()

# Symmetric Difference
print("Symmetric Difference (a ^ b):", a ^ b)  # prints the elements which are not common to both
print("Symmetric Difference using method:", a.symmetric_difference(b))
print()

print("*********************************************")

# Other Set Methods
print("Length of set a:", len(a))
print("Is 2 in set a?", 2 in a)
print("Is set a disjoint with set b?", a.isdisjoint(b))     # if two sets are disjoint are then it will return true, otherwise it will be false
print("Is a subset of b?", a.issubset(b))
print("Is a superset of b?", a.issuperset(b))
print("Is a ∩ b a subset of a?", (a & b).issubset(a))
print("Is a ∩ b a subset of b?", (a & b).issubset(b))

print("*********************************************")

# Clearing a set
a.clear()
print("Set a after clear():", a)
