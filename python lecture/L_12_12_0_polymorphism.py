# polymorphism
# operator overloading -- when the same operator is allowed to have different meaning according to the context

"""DUNDER FUNCTIONS"""
# ─────────────────────────────────────────────────────────────
#   PYTHON DUNDER (MAGIC) METHODS QUICK REFERENCE
# ─────────────────────────────────────────────────────────────
# Object Initialization & Representation
# __init__      → Called when object is created (constructor)
# __del__       → Called when object is deleted (destructor)
# __str__       → User-friendly string (for print)
# __repr__      → Official string (for debugging/developers)

# Object Comparison
# __eq__        → == 
# __ne__        → != 
# __lt__        → < 
# __le__        → <= 
# __gt__        → > 
# __ge__        → >= 

# Arithmetic Operators
# __add__       → + 
# __sub__       → - 
# __mul__       → * 
# __truediv__   → / 
# __floordiv__  → // 
# __mod__       → % 
# __pow__       → **

# In-place Arithmetic
# __iadd__      → += 
# __isub__      → -= 
# __imul__      → *= 
# __itruediv__  → /=

# Container/Sequence Behavior
# __len__       → len(obj) 
# __getitem__   → obj[key] 
# __setitem__   → obj[key] = value 
# __delitem__   → del obj[key] 
# __iter__      → for x in obj 
# __next__      → next(iterator) 
# __contains__  → in operator

# Attribute Handling
# __getattr__   → Called when attribute not found
# __setattr__   → Called when attribute is set
# __delattr__   → Called when attribute deleted
# __dir__       → Called when dir(obj) is used

# Callable / Context Manager
# __call__      → obj() makes object callable
# __enter__     → with obj: (setup)
# __exit__      → with obj: (teardown)

# Others
# __bool__      → bool(obj) 
# __hash__      → hash(obj) (used in sets/dicts) 
# __copy__      → copy.copy(obj) 
# __deepcopy__  → copy.deepcopy(obj) 
# __index__     → Converts to int when needed (e.g., slicing)
# ─────────────────────────────────────────────────────────────



print(1 + 2)
print('my' + 'school')      # called concatenate
print([1,2,3] + [4,5,6])    # called merge
# here + is applicable for all different types data types, hence called operator overaloading

print("*********************************************************************************")

class Complex:
    def __init__(self, A, B):
        self.A = A
        self.B = B
    
    def show(self):
        print(self.A, 'i +', self.B, 'j')

    # type 1
    def add(self, x):
        newA = self.A + x.A 
        newB = self.A + x.B 

        return Complex(newA, newB)

    # type 2
    def add2(self, x, y):
        newA = x.A + y.A
        newB = x.B + y.B 

        return Complex(newA, newB)

n1 = Complex(1, 3)
n1.show()
print()

n2 = Complex(4, 6)
n2.show()

n3 = n1.add(n2)     # returns an object, hence n3 became an object

n3.show()

print()
n4 = n3.add2(n3, n2)
n4.show()

print("**********************************************************************")













