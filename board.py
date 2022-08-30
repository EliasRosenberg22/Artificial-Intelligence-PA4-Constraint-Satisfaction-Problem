#Author: Elias Rosenberg
#Date: October 21, 2021
#Purpose: Create a class to hold the values for a board object for the circuit board csp.

class Board:
    def __init__(self, length, width, character, components):
        self.length = length
        self.width = width
        self.character = character #the character that blank pieces of the board are represented by
        self.components = components #list of component objects to add
        self.component_dict = {} #drawing
        self.positions = {} #dict of components to the coord of of each components bottom left character
        self.coords_list = []
        self.ascii_board = ""
        print(len(self.components))

        for x in range(0, self.width):
            for y in range(0, self.length):
                self.coords_list.append((x, y))

    # adds a component to the board, puts its location in the drawing
    def add_component(self, component):
        if self.is_valid(component, component.placement):
            self.component_dict[component.char] = []
            for x in range(component.placement[0], component.placement[1]):
                for y in range(component.placement[2], component.placement[3]):
                    self.component_dict[component.char].append((x, y))

    # checks that each space occupied in this placement is not already occupied
    def is_valid(self, component, placement):
        for x in range(placement[0], placement[1]):
            for y in range(placement[2], placement[3]):
                for comp in self.component_dict:
                    if comp != component:
                        if (x, y) in self.component_dict[comp]:
                            return False
        return True

    # for each x and y in the board see if there's a component there and print its character, if not print a dot
    def __str__(self):
        s = ""
        for y in range(self.length):
            for x in range(self.width):
                drawn = False
                for char in self.component_dict:
                    if (x, y) in self.component_dict[char]:
                        s += char
                        drawn = True
                if not drawn:
                    s += '.'
            s += "\n"
        return s
