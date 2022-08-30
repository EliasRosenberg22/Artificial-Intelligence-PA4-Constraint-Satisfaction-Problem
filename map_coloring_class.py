#Author: Elias Rosenberg
#Date October 18th, 2021
#Purpose: Creates a specific Map coloring CSP that holds all the specifc domain and variable names, as well as the helper
#methods needed to find neighbors and number of legal states, etc.

from variable import Variable
from general_csp import CSP
from constraint import *
from csp_algorithms import *


class Map_Coloring_CSP:
    def __init__(self, variables, domains, neighbor_dict):
        self.variables = variables
        self.domains = domains
        self.constraints = {} #maps a state's name as a key to all constraints
        self.neighbor_dict = neighbor_dict #maps a state's name as a key to all neighbors, given when the class is constructed
        for var in self.variables:
            self.constraints[var] = []

    def add_constraint(self, constraint, variable):
        self.constraints[variable].append(
            constraint)  # add the constraint to the list of constraints for that variable


    def get_neighbors(self, variable):
        return self.neighbor_dict[variable]


if __name__ == '__main__':

    WA = Variable("Western Australia",  domain = ['red', 'green', 'blue'])
    NT = Variable("Northern Territory",  domain = ['red', 'green', 'blue'])
    SA = Variable("South Australia",  domain = ['red', 'green', 'blue'])
    Q = Variable("Queensland",  domain = ['red', 'green', 'blue'])
    NSW = Variable("New South Wales",  domain = ['red', 'green', 'blue'])
    V = Variable("Victoria",  domain = ['red', 'green', 'blue'])
    T = Variable ("Tasmania",  domain = ['red', 'green', 'blue'])


    domain = ['red', 'green', 'blue']
    domains = {}
    variables = [WA.name, NT.name, SA.name, Q.name, NSW.name, V.name, T.name]
    variables1 = [WA, NT, SA, Q, NSW, V, T]
    neighbor_dict = {}
    for name in variables:
        neighbor_dict[name] = []
        domains[name] = domain[:]

    neighbor_dict["Western Australia"] = ["Northern Territory" , "South Australia"]
    neighbor_dict["Northern Terriroty"] = ["Western Australia", "South Australia", "Queensland"]
    neighbor_dict["South Australia"] = ["Western Australia", "Northern Territory", "Queensland", "New South Wales", "Victoria"]
    neighbor_dict["Queensland"] = ["Northern Territory", "South Australia", "New South Wales"]
    neighbor_dict["Victoria"] = ["South Australia", "New South Wales"]
    neighbor_dict["Tasmania"] = []


    MapCSP = Map_Coloring_CSP(variables, domains, neighbor_dict)
    algos = CSP_algorithms(MapCSP)
    test_assignment = {}

    for var in variables:
        algos.add_constraint(Constraint("Western Australia", "Northern Territory"), var)
        algos.add_constraint(Constraint("Western Australia", "South Australia"), var)
        algos.add_constraint(Constraint("South Australia", "Northern Territory"), var)
        algos.add_constraint(Constraint("Queensland", "Northern Territory"), var)
        algos.add_constraint(Constraint("Queensland", "South Australia"), var)
        algos.add_constraint(Constraint("Queensland", "New South Wales"), var)
        algos.add_constraint(Constraint("New South Wales", "South Australia"), var)
        algos.add_constraint(Constraint("Victoria", "South Australia"), var)
        algos.add_constraint(Constraint("Victoria", "New South Wales"), var)
        algos.add_constraint(Constraint("Victoria", "Tasmania"), var)

    solution = algos.backtrack(test_assignment)
    print(solution)





