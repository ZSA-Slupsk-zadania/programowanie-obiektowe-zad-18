from abc import ABC, abstractmethod

class Shape(ABC):

    type = None

    def __init__(self, type):
        self.type = type

    def __del__(self):
        print("Destructor called")

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def display(self):
        pass

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type