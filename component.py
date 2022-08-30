#Author Elias Rosenberg
#Date: October 21, 2021
#Purpose: Create a class for the circuit board problem that represents a component on the board. Location holds the components
#coords of the bottom left-hand corner.

class Component:
    def __init__(self, length, width, letter):
        self.length = length
        self.width = width
        self.letter = letter # where each component has a certain character

class Location:

    def __init__(self, x, y):
        self.x = x
        self.y = y