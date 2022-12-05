# define rubix cube puzzle

class RubixCube: 
    def __init__(
        self,
        n = 3, # n*n*n size rubik's Cube
        colours = ['white', 'orange', 'red', 'blue', 'yellow'],    # colors for each face of the cube
        stat = None,  # string represent the curr stat of the cube
    ):
        self.n = n
        self.colours = colours
        self.reset()
        
    # initialize the cube 
    def reset(self):
        self.cube = [[[c for x in range(self.n)] for y in range(self.n)] for c in self.colours]  # create the cube as solved version 

    # function to check if the cube is solved
    def is_solved(self):
        pass

    # shuffle the cube
    def shuffle(self, n):
        pass

    # horizontal twist
    def horizontal_twist(self, face, direction):
        pass

    # vertical twist
    def vertical_twist(self, face, direction):
        pass

    # side twist
    def side_twist(self, face, direction):
        pass

    # print the cube
    def print_cube(self):
        pass