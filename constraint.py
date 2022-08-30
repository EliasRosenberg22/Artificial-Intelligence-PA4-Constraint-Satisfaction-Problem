#Author: Elias Rosenberg
#Date: October 17, 2021
#Purpose: Create a class that models the constraint for the map-coloring problem. Takes the names of two territories. If the colors of the locations
#are the same then a constraint is being broken.

class Constraint:

    def __init__(self, loc1, loc2):
        self.loc1 = loc1
        self.loc2 = loc2
        self.variables = [loc1, loc2]
        self.constraint_dict = {}

    # creates a generic constraint dictionary of variables to list of constraints because each variable has a constraint list. What determines a constraint needs to be defined in the more specific problem class.
    def create_constraint_dict(self):
        for variable in self.variables:
            self.constraint_dict[variable] = [] #the key is the variable, not the variable.name. May have to change that

        return self.constraint_dict

    def satisfied(self, assignment):
        if self.loc1 not in assignment or self.loc2 not in assignment:
            return True

        return assignment[self.loc1] != assignment[self.loc2]
