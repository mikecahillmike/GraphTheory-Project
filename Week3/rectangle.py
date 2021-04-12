class Rectangle:
    # Member vaiables (Dont need this as constructor will create them auto)
    height = 0
    width = 0
    # Constructor __init__
    def __init__(self, height, width):
        self.height = height
        self.width = width
    # Calculate the area
    def area(self):
        return self.height * self.width
    # Calculate the perimeter
    def perimeter(self):
        p = (2 * self.height) + (2 * self.width)
        return p

# Create instance
r1 = Rectangle(10, 35)
r1.height = 20

# Another instance
r2 = Rectangle(2, 5)

print(f"Area of r1 = {r1.height} x {r1.width} = {r1.area()}")
print(f"Area of r1 = {r2.height} x {r2.width} = {r2.area()}")
print("The perimeter of the rectangle is", r2.perimeter())