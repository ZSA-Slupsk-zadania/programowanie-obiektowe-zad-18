from shape import Shape
from shapes import Rectangle, Square, Circle
from graphics import Graphics

# Create graphics object
graphics = Graphics()

# Create shapes
rectangle = Rectangle("Rectangle", 10, 5)
square = Square("Square", 5)
circle = Circle("Circle", 5)

# Add shapes to graphics object
graphics.addShape(rectangle)
graphics.addShape(square)
graphics.addShape(circle)

# Draw shapes
graphics.draw()