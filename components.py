#This will be the Components class which serves as the base class for the main components
#Contributor: Luis Orellana

# Abstract Base Class module
from abc import ABC, abstractmethod

class Components(ABC):
    # Constructor
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def update(self):
        pass
