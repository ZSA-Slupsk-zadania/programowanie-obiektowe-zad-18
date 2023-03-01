from shape import Shape

# Implement Shape class creating different shapes
# Make use of type abstract field
# Make use of area, perimeter and display abstract methods

class Rectangle(Shape):
    
        def __init__(self, type, length, width):
            super().__init__(type)
            self.length = length
            self.width = width
    
        def area(self):
            return self.length * self.width
    
        def perimeter(self):
            return 2 * (self.length + self.width)
    
        def display(self):
            print("Type: " + self.type)
            print("Length: " + str(self.length))
            print("Width: " + str(self.width))
            print("Area: " + str(self.area()))
            print("Perimeter: " + str(self.perimeter()))

class Square(Shape):

    def __init__(self, type, side):
        super().__init__(type)
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

    def display(self):
        print("Type: " + self.type)
        print("Side: " + str(self.side))
        print("Area: " + str(self.area()))
        print("Perimeter: " + str(self.perimeter()))

class Circle(Shape):

    def __init__(self, type, radius):
        super().__init__(type)
        self.radius = radius

    def area(self):
        return 3.14 * (self.radius ** 2)

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def display(self):
        print("Type: " + self.type)
        print("Radius: " + str(self.radius))
        print("Area: " + str(self.area()))
        print("Perimeter: " + str(self.perimeter()))