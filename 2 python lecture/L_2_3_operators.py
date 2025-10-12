# Python Operators with Examples

# 1. Arithmetic Operators
print("=== Arithmetic Operators ===")
a, b = 10, 3
print("a + b =", a + b)    # Addition
print("a - b =", a - b)    # Subtraction
print("a * b =", a * b)    # Multiplication
print("a / b =", a / b)    # Division
print("a % b =", a % b)    # Modulus
print("a ** b =", a ** b)  # Exponentiation
print("a // b =", a // b)  # Floor division
print()

# 2. Comparison Operators
print("=== Comparison Operators ===")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
print()

# 3. Logical Operators
print("=== Logical Operators ===")
x, y = True, False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)    # not true = false (bcoz x is originally assigned true, hence it became false)
print("not y", not y)     # not true = true
print()

# 4. Bitwise Operators
print("=== Bitwise Operators ===")
m, n = 5, 3  # Binary: 101 and 011
print("m & n =", m & n)   # AND
print("m | n =", m | n)   # OR
print("m ^ n =", m ^ n)   # XOR
print("~m =", ~m)         # NOT
print("m << 1 =", m << 1) # Left shift
print("m >> 1 =", m >> 1) # Right shift
print()

# 5. Assignment Operators
print("=== Assignment Operators ===")

# Arithmetic assignment examples
p = 10
print("Initial p:", p)
p += 5
print("p += 5:", p)
p -= 3
print("p -= 3:", p)
p *= 2
print("p *= 2:", p)
p /= 4
print("p /= 4:", p)
p %= 3
print("p %= 3:", p)
p //= 2
print("p //= 2:", p)
p **= 3
print("p **= 3:", p)

# Reset p as integer for bitwise assignments
p = 5
print("\nReset p for bitwise assignment:", p)
p &= 2
print("p &= 2:", p)
p |= 5
print("p |= 5:", p)
p ^= 1
print("p ^= 1:", p)
p <<= 1
print("p <<= 1:", p)
p >>= 1
print("p >>= 1:", p)
print()

# 6. Identity Operators
print("=== Identity Operators ===")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 is list2:", list1 is list2)       # False (different objects)
print("list1 is list3:", list1 is list3)       # True (same object)
print("list1 is not list2:", list1 is not list2)
print()

# 7. Membership Operators
print("=== Membership Operators ===")
nums = [1, 2, 3, 4, 5]
print("3 in nums:", 3 in nums)
print("10 in nums:", 10 in nums)
print("10 not in nums:", 10 not in nums)
