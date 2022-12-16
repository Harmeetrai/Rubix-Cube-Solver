# define rubix cube puzzle
from random import randint, choice


class RubixCube:
    def __init__(
        self,
        n=3,  # n*n*n size rubik's Cube
        colours=['w', 'o', 'g', 'r', 'b', 'y'],
        state=None,  # string represent the curr stat of the cube
    ):
        if state is None:
            self.n = n
            self.colours = colours
            self.reset()
        else:
            self.n = int((len(state) / 6) ** (.5))
            self.colours = []
            self.cube = [[[]]]
            for i, s in enumerate(state):
                if s not in self.colours:
                    self.colours.append(s)
                self.cube[-1][-1].append(s)
                if len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) < self.n:
                    self.cube[-1].append([])
                elif len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) == self.n and i < len(state) - 1:
                    self.cube.append([[]])

    # initialize the cube
    def reset(self):
        self.cube = [[[c for x in range(self.n)] for y in range(
            self.n)] for c in self.colours]  # create the cube as solved version

    # function to check if the cube is solved (solved will return 0, unsolved return 1)
    def is_solved(self):
        for side in self.cube:
            check_solve = 0
            hold = []
            for row in side:
                if len(set(row)) == 1:
                    hold.append(row[0])
                else:
                    check_solve = 1
                    break
            if check_solve == 1:
                break
            if len(set(hold)) > 1:
                check_solve = 1
                break
        return check_solve

        # pass

    def stringify(self):
        """
        Input: None
        Description: Create string representation of the current state of the cube
        Output: string representing the cube current state
        """
        return ''.join([i for r in self.cube for s in r for i in s])

    # print the cube
    def print_cube(self):
        spacing = f'{" " * (len(str(self.cube[0][0])) + 2)}'
        l1 = '\n'.join(spacing + str(c) for c in self.cube[0])
        l2 = '\n'.join('  '.join(str(self.cube[i][j]) for i in range(
            1, 5)) for j in range(len(self.cube[0])))
        l3 = '\n'.join(spacing + str(c) for c in self.cube[5])
        print(f'{l1}\n\n{l2}\n\n{l3}')

    # shuffle the cube
    # lower and upper bound is for min and max moves
    def shuffle(self):
        actions = [
            ('h', 0),
            ('h', 1),
            ('v', 0),
            ('v', 1),
            ('s', 0),
            ('s', 1)
        ]
        moves = randint(5, 100)
        for i in range(moves):
            a = choice(actions)
            j = randint(0, self.n - 1)
            if a[0] == 'h':
                self.horizontal_twist(j, a[1])
            elif a[0] == 'v':
                self.vertical_twist(j, a[1])
            elif a[0] == 's':
                self.side_twist(j, a[1])
       # pass

    # horizontal twist
    # direction is for left ( 0 ) or counter right ( 1 )
    def horizontal_twist(self, row, direction):
        if row < len(self.cube[0]):
            if direction == 0:  # Twist left
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[2][row],
                                                                                              self.cube[3][row],
                                                                                              self.cube[4][row],
                                                                                              self.cube[1][row])

            elif direction == 1:  # Twist right
                self.cube[1][row], self.cube[2][row], self.cube[3][row], self.cube[4][row] = (self.cube[4][row],
                                                                                              self.cube[1][row],
                                                                                              self.cube[2][row],
                                                                                              self.cube[3][row])
            else:
                return
            if direction == 0:  # Twist left
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(
                        *reversed(self.cube[0]))]  # Transpose top
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(
                        *reversed(self.cube[5]))]  # Transpose bottom
            elif direction == 1:  # Twist right
                if row == 0:
                    self.cube[0] = [list(x) for x in zip(
                        *self.cube[0])][::-1]  # Transpose top
                elif row == len(self.cube[0]) - 1:
                    self.cube[5] = [list(x) for x in zip(
                        *self.cube[5])][::-1]  # Transpose bottom
        else:
            return
       # pass

    # vertical twist
    # direction is for down( 0 ) or counter up ( 1 )
    def vertical_twist(self, col, direction):
        if col < len(self.cube[0]):
            for i in range(len(self.cube[0])):
                if direction == 0:  # Twist down
                    self.cube[0][i][col], self.cube[2][i][col], self.cube[4][-i-1][-col-1], self.cube[5][i][col] = (self.cube[4][-i-1][-col-1],
                                                                                                                    self.cube[0][i][col],
                                                                                                                    self.cube[5][i][col],
                                                                                                                    self.cube[2][i][col])
                elif direction == 1:  # Twist up
                    self.cube[0][i][col], self.cube[2][i][col], self.cube[4][-i-1][-col-1], self.cube[5][i][col] = (self.cube[2][i][col],
                                                                                                                    self.cube[5][i][col],
                                                                                                                    self.cube[0][i][col],
                                                                                                                    self.cube[4][-i-1][-col-1])
                else:
                    return
            if direction == 0:  # Twist down
                if col == 0:
                    self.cube[1] = [list(x) for x in zip(
                        *self.cube[1])][::-1]  # Transpose left
                elif col == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for x in zip(
                        *self.cube[3])][::-1]  # Transpose right
            elif direction == 1:  # Twist up
                if col == 0:
                    self.cube[1] = [list(x) for x in zip(
                        *reversed(self.cube[1]))]  # Transpose left
                elif col == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for x in zip(
                        *reversed(self.cube[3]))]  # Transpose right
        else:
            return
        # pass

    # side twist
    # direction is for down( 0 ) or counter up ( 1 )
    def side_twist(self, col, direction):
        if col < len(self.cube[0]):
            for i in range(len(self.cube[0])):
                if direction == 0:  # Twist down
                    self.cube[0][col][i], self.cube[1][-i-1][col], self.cube[3][i][-col-1], self.cube[5][-col-1][-1-i] = (self.cube[3][i][-col-1],
                                                                                                                          self.cube[0][col][i],
                                                                                                                          self.cube[
                                                                                                                              5][-col-1][-1-i],
                                                                                                                          self.cube[1][-i-1][col])
                elif direction == 1:  # Twist up
                    self.cube[0][col][i], self.cube[1][-i-1][col], self.cube[3][i][-col-1], self.cube[5][-col-1][-1-i] = (self.cube[1][-i-1][col],
                                                                                                                          self.cube[
                                                                                                                              5][-col-1][-1-i],
                                                                                                                          self.cube[0][col][i],
                                                                                                                          self.cube[3][i][-col-1])
                else:
                    return
            if direction == 0:  # Twist down
                if col == 0:
                    self.cube[4] = [list(x) for x in zip(
                        *reversed(self.cube[4]))]  # Transpose back
                elif col == len(self.cube[0]) - 1:
                    self.cube[2] = [list(x) for x in zip(
                        *reversed(self.cube[2]))]  # Transpose top
            elif direction == 1:  # Twist up
                if col == 0:
                    self.cube[4] = [list(x) for x in zip(
                        *self.cube[4])][::-1]  # Transpose back
                elif col == len(self.cube[0]) - 1:
                    self.cube[2] = [list(x) for x in zip(
                        *self.cube[2])][::-1]  # Transpose top
        else:
            return
        # pass
