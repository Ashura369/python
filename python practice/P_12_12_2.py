# make a "Order" class assign item and price
# now use "__gt__" to check wheather the first price is > second price or not

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):        # greater than
        return self.price > other.price

# -------------------------------------------------------------


o1 = Order('Sugar', 40)
o2 = Order('Salt', 30)

print(o2 > o1)

