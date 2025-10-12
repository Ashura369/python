# make a circle class, assign radius and find area and perimeter using method


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):         # pie r square
        temp = (22/7) * (self.radius ** 2)
        temp = round(temp, 2)
        return temp
    
    def perimeter(self):        # 2 pie r
        temp = 2 * (22/7) * self.radius
        temp = round(temp, 2)
        return temp

# ----------------------------------------------------------------

c1 = Circle(25)

print("The area of the circle is",round(c1.area(), 2))

print("The perimeter of the circle is", c1.perimeter())