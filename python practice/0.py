class Complex:
    def __init__(self, A, B):
        self.A = A
        self.B = B
    
    def show(self):
        print(self.A, 'i +', self.B, 'j')

    def add(self, x, y):
        newA = x.A + y.A
        newB = x.B + y.B 

        return Complex(newA, newB)

n1 = Complex(1, 3)
n1.show()
print()

n2 = Complex(4, 6)
n2.show()

n3 = n1.add(n1, n2)
print()

n3.show()