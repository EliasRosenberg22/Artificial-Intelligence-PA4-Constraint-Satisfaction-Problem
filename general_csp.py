#Author: Elias Rosenberg
#Date: October 17, 2021
#Purpose: Create a class that outlines the outlines a general csp with variables, domains, and constraints.

from variable import Variable
from constraint import *

class CSP:
    # takes a list of the variables for the problem, and a dict of variable names to the domain list
    def __init__(self, variables, domains):
        self.variables = variables
        self.domains = domains
        self.constraints = {}
        for var in self.variables:
            self.constraints[var] = []

    def add_constraint(self, constraint, variable):
            self.constraints[variable].append(constraint) #add the constraint to the list of constraints for that variable

