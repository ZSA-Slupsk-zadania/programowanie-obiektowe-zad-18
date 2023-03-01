from shape import Shape

class Graphics: 

    chapeList = []

    def __init__(self, shapeList = []):
        self.chapeList = shapeList

    def addShape(self, shape):
        self.chapeList.append(shape)

    def draw(self):
        for shape in self.chapeList:
            shape.display()