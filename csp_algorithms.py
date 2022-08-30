#Author: Elias Rosenberg
#Date: October 17, 2021
#Purpose: Create a class that outlines all the algorithms needed to solve any given CSP. Backtrack() loops through the
#viable legal assignments to a given state. The heuristics are stored in this class, as well as the arc-consistency algo.

from variable import Variable
from general_csp import CSP
from constraint import *
from map_coloring_class import Map_Coloring_CSP
import timeit

class CSP_algorithms:
    # takes a constraint satisfaction problem to work on. The CSP is pre-built with all variables, domains, and constraints given
    def __init__(self, csp):
        self.csp = csp
        self.variables = csp.variables
        self.domains = csp.domains
        self.constraints = csp.constraints

    def add_constraint(self, constraint, variable):
            self.constraints[variable].append(constraint) #add the constraint to the list of constraints for that variable

    def is_consistent(self, variable, assignment): #if the assignment does not go against any constraint for the variable, it is consistent
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def select_unassigned_var(self, assignment): #changes depending on which heursitc we want to be using. Simplest version picks the first unassigned variable and returns it.
        for variable in self.variables:
            if variable not in assignment:
                return variable
        else:
            print("No unassigned variables. Solution is complete")
            return assignment

    def minimum_remaining_val(self, assignment): #selects the variable with the least 'legal' values as the next to assign
        unassigned = []
        for variable in self.variables:
            if variable not in assignment:
                unassigned.append(variable) #add all the unassigned variables to this list

        min = unassigned[0] #placeholder for the variable with the smallest domain --> least legal values
        for variable in unassigned:
            if len(variable.domain) < len(min.domain): #If this variable has a smaller domain, set it equal to min.
                min = variable
        return min

    def degree_heurustic(self, assignment): #selects the variable that affects the most neighbors
        unassigned = []
        for variable in self.variables:
            if variable not in assignment:
                unassigned.append(variable) #add all the unassigned variables to this list. (Needs to be rebuilt everytime because the assignment is different every time)

        most_neighbors = unassigned[0]
        max = 0
        for variable in unassigned:
            neighbor_count = 0
            for neighbor in self.csp.get_neighbors(variable): #utilizes helper function in csp to get the number of neighbors. get_neighbors is built in the specifc csp class, and returns a list of neighbors of a state.
                if neighbor in unassigned:
                    neighbor_count += 1

            if neighbor_count > max:
                max = neighbor_count
                most_neighbors = variable
        return most_neighbors


    #inference function
    def AC3(self, assignment, queue=None): #worked on this with a TA.
        if queue == None:
            queue = [(x, y) for x in self.variables for y in self.csp.get_neighbors(x)]
            #print(queue)

        while queue:
            (x, y) = queue.pop()
            domains = self.domains[x].copy()

            if self.remove_inconsistent(x, y, assignment):
                if len(self.domains[x]) == 0:
                    self.domains[x] = domains
                    return False

                for nx in self.csp.get_neighbors(x):
                    queue.append((nx, y))
        return True

        # removes inconsistent possible assignments
    def remove_inconsistent(self, x, y, assignment): #helper function to remove illegal domain values for a given pair of variables.
        removed = False
        for a in self.domains[x]:
            new = assignment.copy()
            new[x] = a
            n = len(self.csp.possible_values(y, new))

            if n == 0:
                if len(self.domains[x]) > 0:
                    self.domains[x].remove(a)
                    removed = True
        return removed

    def backtrack(self, assignment={}): #backtracking algorithm to solve given csp.
        start = timeit.default_timer()
        if len(assignment) == len(self.variables): #if the assignment is as long as the list of variables, every variable must have been assigned
            return assignment

        val = self.degree_heurustic(assignment) #change this line to other heursitc methods to get different outcomes. Must implement the specific helper functions in each problem class.
        for value in self.domains[val]:
            assignment[val] = value

            #ac3 = self.AC3(self.csp, local_assignment) #uncomment this line to use AC3
            #if ac3:
            if self.is_consistent(val, assignment):
                result = self.backtrack(assignment)
                if result:

                    stop = timeit.default_timer()
                    print('Time: ', stop - start) #timer to check runtime in heursitc comparisons
                    return result

            del assignment[val]

        #stop = timeit.default_timer()
        #print('Time: ', stop - start)



