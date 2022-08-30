#Author: Elias Rosenberg
#Date: October 17, 2021
#Purpose: Create a class that outlines a generic variable object for a CSP

class Variable:


    def __init__(self, name, domain):
        self.name = name #name of the variable (either a territory for the map-coloring problem, or a circuit piece)
        self.domain = domain #domain of the variable, given as a list of integers
        self.value = None #the eventual value of this variable after back-tracking


    def is_assigned(self): #just to check if the variable has an assignment --> backtracking debugging
        if self.value == None:
            print("there is still no value, just checking")
            return False
        else:
            print("The value of " + str(self.name) + " is " + self.value)
            return True








