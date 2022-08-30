#Author: Elias Rosenberg
#Date: October 21, 2021
#Purpose: Create all the classes and and methods necessary for solving the circuit board problem utilizing CSP algorithms
#implemented in csp_algorit hms.py

from board import Board
from component import Component, Location
from csp_algorithms import *

class Constraint:
    def __init__(self, comp1, comp2):
        self.comp1 = comp1
        self.comp2 = comp2

    def satisfied(self, assignment):
        if self.comp1 not in assignment or self.comp2 not in assignment:
            return True
        loc1 = assignment[self.comp1]
        loc2 = assignment[self.comp2]

        if loc1.x == loc2.x and loc1.y == loc2.y: #if the coords are the same, the components must be overlapping.
            return False

        if loc1.x == loc2.x:
            if loc2.y > loc1.y and loc2.y - (self.comp2.length-1) <= loc1.y: #when the x values are the same one component may overlap vertically
                return False

            if loc2.y < loc1.y and loc1.y - (self.comp1.length-1) <= loc2.y:
                return False

        if loc1.y == loc2.y:
            if loc2.x > loc1.x and loc2.x <= loc1.x + (self.comp1.width-1): #when the y values are the same one component may overlap horizontally
                return False

            if loc2.x < loc1.x and loc1.x <= loc2.x + (self.comp2.width-1):
                return False


        if loc1.x < loc2.x and loc1.y > loc2.y: #These check if any of the four corners of one component is overlapping with the corners of another component.
            if loc2.x <= loc1.x + (self.comp1.width-1) and loc2.y >= loc1.y - (self.comp1.length-1):
                return False

        if loc1.x > loc2.x and loc1.y < loc2.y:
            if loc1.x <= loc2.x + (self.comp2.width-1) and loc1.y >= loc2.y - (self.comp2.length-1):
                return False

        if loc2.x < loc1.x and loc2.y < loc1.y:
             if loc2.x + (self.comp2.width-1) >= loc1.x and loc1.y - (self.comp1.length-1) <= loc2.y:
                 return False

        if loc1.x < loc2.x and loc1.y < loc2.y:
            if loc1.x + (self.comp1.width-1) >= loc2.x and loc2.y - (self.comp2.length-1) <= loc1.y:
                return False

        return True


class Circuit_Board_CSP:
    def __init__(self, board, components):
        self.board = board
        self.variables = components
        self.assignment = {}
        self.domains = {}
        self.constraints = {}

        for component in self.variables:  # add possible assignments. Worked through all of this with a TA because I couldn't figure it out :/
            self.domains[component] = []
            l = component.length
            w = component.width

            # for each x and y on the board
            for x in range(board.width-w+1):
                for y in range(l-1, board.length):
                    self.domains[component].append(Location(x, y))

        for var in self.variables:
            self.constraints[var] = []
            for var2 in self.variables:
                if var.letter != var2.letter:
                    self.constraints[var].append(Constraint(var, var2))

    def add_constraint(self, constraint, variable):
        self.constraints[variable].append(
            constraint)  # add the constraint to the list of constraints for that variable


    def is_valid(self, component, assignment):
        board = Board(self.board.l, self.board.w, '.', self.variables)
        for comp in assignment:
            placement = assignment[comp]
            self.variables[comp].placement = placement
            board.add_component(self.variables[comp])
        if board.is_valid(component, component.position):
            return True
        return False

    # get neighbors of a variable (all the components)
    def get_neighbors(self, component):
        neighbors = []
        for comp in self.variables:
            if comp != component:
                neighbors.append(comp)
        return neighbors


if __name__ == '__main__':
    components = [Component(3, 1, 'a'), Component(3, 2, 'b')]
    board = Board(3, 3, '.', components)
    cpb = Circuit_Board_CSP(board, components)
    algos = CSP_algorithms(cpb)
    res = algos.backtrack()

    height = 3
    width = 3
    board = [["." for _ in range(width)] for _ in range(height)]

    if res:
        for var in res:
            for y in range(res[var].y - var.length + 1, res[var].y + 1):
                for x in range(res[var].x, res[var].x + var.width):
                    board[y][x] = var.letter

        for y in board:
            for x in y:
                print(x, end="")
            print()
    else:
        print("No solution found!")




