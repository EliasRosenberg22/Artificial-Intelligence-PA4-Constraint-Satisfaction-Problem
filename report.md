# Constraint Satisfaction Problem
#Elias Rosenberg
#October 23rd, 2021
#21F
#Quattrini li
#COSC 76

# Introduction

In this lab we were tasked with modeling a general format for solving constraint satisfaction problems. By Generalizing the backtracking and satisfaction algorithms, we can solve any csp by modeling the distinct problem as a new object tailored to that problem. Every problem object takes a list of Variables, each with their own list of possible values in their domain. Every problem also takes its own definition of what a constraint is. 

# Description:
The backtracking algorithm runs through all of the unassigned variables and checks to see if any value in their domain is "consistent" with all the other assigned variables; that value doesn't doesn't conflict with any of the pre-determined constraints. In the map coloring problem, each terriroy in australia is assigned a color–red, green, or blue–and no two neighboring territories can have the same color. For the first pass of the backtracking algorithm, since no variables are assigned, the first color for the first state is usually red (depending upon heuristics that I will cover soon). Since that state is now red, its neighbors can either be blue or green. Those colors are picked and the algorithm keeps going through unassigned states until all are colored. 

In the backtracking pseudocode given in the text-book, there is a 'select-unassigned' method that chooses which variable to give a value to next. This method is what changes when we determine what heuristic we want for the search problem. The easiest thing to do is to create a list of unassigned variables, and then return the first item in that list to be colored. We can do better. The Minimum-Remaining-Value heuristic, or MRV, returns the variable that has the least legal values left to chose from. This allows us to stop unsuccessful attmepts at solving the problem early, because if there is a variable with no legal coloring options, that variable will be returned first and 'no solution possible' will be returned. The degree heuristic returns the variable with the most constraints. In this setup, that means the variable with most neighbors. This is useful becuase assigning a value to a state that has the most neighbors locks in the values for all those other states, cutting down the possible state-space. The Least-Constraining-Value heuristic is kind of like the opposite of the degree heuristic, chosing the state that forces the coloring of the fewest neighbors. 

The map coloring problem doesn't vary in run-time with the use of different heuristics because it is not dealing with that much data to begin with. The heuristcs do cause the results to change. When picking the first unassigned Variable to begin with, Western Australia is always red. When using the heuristics, however, it was usually green, suggesting that the heuristics were returning more optimal solutions.

The final algorithm we had to implement for this lab was Arc-Consistency. Arc-Consistency 3, or AC3, was another helper function that laid within the backtracking algorithm and is designed to remove erroneous variable posibilities between any two neighbors. Technically, arc consistency shouldn't do much for the map coloring problem, because no matter what values you get rid of in the domain of one variable there is always another answer for the second variable. For a more specific csp where not all the variables have the same domains, AC3 goes through every the domains of every pair of variables, making sure that there are no assignments such that those two variables break any constraints. Once all the illegal assignments are removed between every pair of variables, the search problem is said to be 'arc-consistent' because all the arc relationships between any two variables have values in their domains that are all consistent. 

So much of getting this lab to work was planning how the csp object interacted with the algoritm class. Because there was no given code, and many facets of the lab had no pseudocode to go off of in the textbook, planning how pieces interacted with eachother before was paramount. Only after talking with a TA did I find out that it was better to hold all the search algorithms and heursistics in one seperate class to make things easier. At first I was testing the map coloring problem in the same class that I held the algorithms in, which was a mess when I realized I needed specific helper functions in the map csp class that made the heuristics work for that problem. 

Implementing the circuit-board problem was really hard for me, and is the reason I had to use a late day. Going through all the cases of circuit board overlap in the is-consistent() method took a very long time. I consulted a friend on this, and he had the brilliant idea of storing the circuit board's location within a seperate Location object that stored x and y instead just assigning it a tuple. This fixed all of the iterable debug errors I was getting, and salvaged my whole implementation. 

# Evaluation: 

Yes the algorithms work well. Unless there is no solution possible, I have always gotten back an answer to both the map-coloring and circuit board problems given reasonable variables and domains. My biggest failure of this lab was never getting the LCV heuristic to work. I couldn't wrap my head around how to count the change in neighbors's domains based on an assignment to one variable, and then looping through every variable to see which one strong-arms the least amount of neighbors. Couldn't you only get that information through backtracking to get assignments? I'm guessing this could have been solved through some helper function that gave neighbors temporary assignments, but I didn't have the time to stop and figure it out. 

The algorithms were the slowest when no heuristics were used, and were the fastest when using degree heuristic in conjuction with arc consistency. Arc consistency didn't affec the map-coloring problem at all, but cut the runtime for the circuit board problem by nearly half. 

Map Coloring Problem: 
No heuristic: 9.147499999999364e-05 seconds
MRV: 4.2831999999992654e-05
LCV: N/A
Degree heuristic: 8.728999999998988e-06 seconds
Arc Consistency:  9.494599999999853e-05 seconds

Circuit Board Problem: 
No heuristic: 6.46990000000014e-05
Degree heuristic: 2.734700000001089e-05
MRV: 7.815400000001083e-05
LCV: N/A
Arc Consistency: 2.3229999999999085e-05

All of these values changed during every run of the algorithms, but this is the general trend that I noticed after many runs. Honestly, every run was so quick since there's so little data to be run through, heuristics and arc-consistency weren't needed to improve these problems at all. 

# Discussion Questions: 


1. The timing results of the map solver with and without heuristics were all very fast. The heuristics affected the order in which variables were assigned, which led to more interesting outcomes, as I described above. As hinted at in the textbook, inference did nothing to change the output of the map-coloring problem. 



2. The domain of every variable in the circuit board problem is any possible placement for that variable in the board depending upon its shape and size. Take a 3x3 board with a 1x1 piece. The piece will never be placed on the edges of the top and left sides of the board, because it's size of 1x1 will have parts sticking off the sides of the board. The domain for that 1x1 piece is every point on the board where the component can fit fully. This idea was achieved through the code below

            self.domains[component] = []
            l = component.length
            w = component.width

            # for each x and y on the board
            for x in range(board.width-w+1):
                for y in range(l-1, board.length):
                    self.domains[component].append(Location(x, y))


3. There are seven possible cases for two components overlapping in the circuit board problem. The x and y's of the two components are the same. There are four variaions on two similar situations: when the x's are the same and when the y's are the same. If the x's are the same then one component is on top and another is below. If the y's are the same then either component may overlap another on the left or right. Recall in school when you had to draw a 3d cube on paper, how you layered two squares on top of one another and then connected the lines. This overalapping problem can be visualized like that. Either the bottom left-hand corners of both squares are the same, so we know they're overlapping. Or the squares overlap on just the vertical axis, just the horizontal axis, or on one of four diagonals. This gives us seven possible situations for overlap. 

- lets say that piece 'a' is at (0,0). If piece b is also at (0,0) we know they overlap. We then have two situations: either their x's are the same our their y's are the same. If the y's are the same, then we need to check if the x value of b is between the x value of a + the width of the piece at a. If this is the case, we know that b is overlapping a. We can invert all the values in this case (switching x1 to x2, and component.width1 to 2) to test of component b is overlapping a on its left side (this wouldn't be possible in this case, because component a is at the farmost left side of the board). So in this example, if b was located at (0,2) we know it would overlap with a on the horizontal. This same thinking, of checking if the second component lies in the range between the location of the first component + its width or height needs to be applied to all dimensions to make sure no pieces overlap vertically, horizontally, or diagonally. All cases and the math behind them are shown in this code. 


        if loc1.x == loc2.x and loc1.y == loc2.y:
            return False

        if loc1.x == loc2.x:
            if loc2.y > loc1.y and loc2.y - (self.comp2.length-1) <= loc1.y:
                return False

            if loc2.y < loc1.y and loc1.y - (self.comp1.length-1) <= loc2.y:
                return False

        if loc1.y == loc2.y:
            if loc2.x > loc1.x and loc2.x <= loc1.x + (self.comp1.width-1):
                return False

            if loc2.x < loc1.x and loc1.x <= loc2.x + (self.comp2.width-1):
                return False


        if loc1.x < loc2.x and loc1.y > loc2.y:
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



4. My circuit board problem doesn't do any converting to integers to be parsed in the CSP solver. Based on the way I solved for overlap in the constraints, I only needed to represent each component as the character it was drawn as, and its coordinate stored in a Location object. All the CSP solver does is take variables and see whether or not that variable is legal based on the constraints. If a component is legal based on the overlap constraints, the first legal placement is stored as that variable's placement. My generic solver doesn't opperate on integers. I built it to take variable names into account directly. How constraints are checked is much more important than the backtracking algorithm itself. 