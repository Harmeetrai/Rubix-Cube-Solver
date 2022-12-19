from random import randint, choice


class RubiksCube:
    # Class containing the rubiks cube code
    def __init__(
        self,
        n=3,  # Dimensions of the cube
        # List of colors to be used on the sides of the cube
        sides=['U', 'L', 'F', 'R', 'B', 'D'],
        state=None  # String representation of the current state of the cube
    ):
        """
        Initialize the rubiks cube

        Parameters:
            n (int): Width and height of the rubiks cube
            sides (list): List containing the first letter of every color you wish to use (default = ['U', 'L', 'F', 'R', 'B', 'D'])
            state (str): String representation of the current state of the cube (default = None)

        Returns:
            None
        """
        if state is None:
            self.n = n
            self.sides = sides
            self.reset()
        else:
            self.n = int((len(state) / 6) ** (.5))
            self.sides = []
            self.cube = [[[]]]
            for i, s in enumerate(state):
                if s not in self.sides:
                    self.sides.append(s)
                self.cube[-1][-1].append(s)
                if len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) < self.n:
                    self.cube[-1].append([])
                elif len(self.cube[-1][-1]) == self.n and len(self.cube[-1]) == self.n and i < len(state) - 1:
                    self.cube.append([[]])

    def reset(self):
        """
        Reset the cube to its initial state

        Parameters:
            None

        Returns:
            None
        """
        self.cube = [[[c for x in range(self.n)]
                      for y in range(self.n)] for c in self.sides]

    def solved(self):
        """
        Determine if the cube is solved or not

        Parameters:
            None

        Returns:
            boolean: True if the cube is solved, False otherwise
        """
        for side in self.cube:
            hold = []
            check = True
            for row in side:
                if len(set(row)) == 1:
                    hold.append(row[0])
                else:
                    check = False
                    break
            if check == False:
                break
            if len(set(hold)) > 1:
                check = False
                break
        return check

    def stringify(self):
        """
        Create string representation of the current state of the cube

        Parameters:
            None

        Returns:
            str: String representation of the cube's current state
        """
        return ''.join([i for r in self.cube for s in r for i in s])

    def shuffle(self, move):
        """
        Shuffle the cube

        Parameters:
            move (int): Number of moves to make

        Returns:
            None
        """
        moves = move
        actions = [
            ('h', 0),
            ('h', 1),
            ('v', 0),
            ('v', 1),
            ('s', 0),
            ('s', 1)
        ]
        for i in range(moves):
            a = choice(actions)
            j = randint(0, self.n - 1)
            if a[0] == 'h':
                self.horizontal_twist(j, a[1])
            elif a[0] == 'v':
                self.vertical_twist(j, a[1])
            elif a[0] == 's':
                self.side_twist(j, a[1])

    def show(self):  # Display the Rubik's Cube
        spacing = f'{" " * (len(str(self.cube[0][0])) + 2)}'
        l1 = '\n'.join(spacing + str(c) for c in self.cube[0])
        l2 = '\n'.join('  '.join(str(self.cube[i][j]) for i in range(
            1, 5)) for j in range(len(self.cube[0])))
        l3 = '\n'.join(spacing + str(c) for c in self.cube[5])
        print(f'{l1}\n\n{l2}\n\n{l3}')

        # String representation of the cube
        string = ''
        for x in self.cube[0]:  # Acquires the character from the matrices implemented earlier
            for y in x:        # and adds them to a string in the appropriate order
                for z in y:
                    string += z
        for x in self.cube[3]:
            for y in x:
                for z in y:
                    string += z
        for x in self.cube[2]:
            for y in x:
                for z in y:
                    string += z
        for x in self.cube[5]:
            for y in x:
                for z in y:
                    string += z
        for x in self.cube[1]:
            for y in x:
                for z in y:
                    string += z
        for x in self.cube[4]:
            for y in x:
                for z in y:
                    string += z
        print(string)

    def horizontal_twist(self, row, direction):
        """
        Twist the cube horizontally

        Parameters:
            row (int): Row to twist
            direction (int): Direction to twist (0 = left, 1 = right)

        Returns:
            None
        """
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
                print(f'ERROR - direction must be 0 (left) or 1 (right)')
                return
            # Rotating connected face
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
            print(
                f'ERROR - desired row outside of rubiks cube range. Please select a row between 0-{len(self.cube[0])-1}')
            return

    def vertical_twist(self, column, direction):
        """
        Twist the cube vertically

        Parameters:
            column (int): Column to twist
            direction (int): Direction to twist (0 = down, 1 = up)

        Returns:
            None
        """
        if column < len(self.cube[0]):
            for i in range(len(self.cube[0])):
                if direction == 0:  # Twist down
                    self.cube[0][i][column], self.cube[2][i][column], self.cube[4][-i-1][-column-1], self.cube[5][i][column] = (self.cube[4][-i-1][-column-1],
                                                                                                                                self.cube[0][
                                                                                                                                    i][column],
                                                                                                                                self.cube[5][
                                                                                                                                    i][column],
                                                                                                                                self.cube[2][i][column])
                elif direction == 1:  # Twist up
                    self.cube[0][i][column], self.cube[2][i][column], self.cube[4][-i-1][-column-1], self.cube[5][i][column] = (self.cube[2][i][column],
                                                                                                                                self.cube[5][
                                                                                                                                    i][column],
                                                                                                                                self.cube[0][
                                                                                                                                    i][column],
                                                                                                                                self.cube[4][-i-1][-column-1])
                else:
                    print(f'ERROR - direction must be 0 (down) or 1 (up)')
                    return
            # Rotating connected face
            if direction == 0:  # Twist down
                if column == 0:
                    self.cube[1] = [list(x) for x in zip(
                        *self.cube[1])][::-1]  # Transpose left
                elif column == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for x in zip(
                        *self.cube[3])][::-1]  # Transpose right
            elif direction == 1:  # Twist up
                if column == 0:
                    self.cube[1] = [list(x) for x in zip(
                        *reversed(self.cube[1]))]  # Transpose left
                elif column == len(self.cube[0]) - 1:
                    self.cube[3] = [list(x) for x in zip(
                        *reversed(self.cube[3]))]  # Transpose right
        else:
            print(
                f'ERROR - desired column outside of rubiks cube range. Please select a column between 0-{len(self.cube[0])-1}')
            return

    def side_twist(self, column, direction):
        """
        Twist the cube vertically

        Parameters:
            column (int): Column to twist
            direction (int): Direction to twist (0 = down, 1 = up)

        Returns:
            None
        """
        if column < len(self.cube[0]):
            for i in range(len(self.cube[0])):
                if direction == 0:  # Twist down
                    self.cube[0][column][i], self.cube[1][-i-1][column], self.cube[3][i][-column-1], self.cube[5][-column-1][-1-i] = (self.cube[3][i][-column-1],
                                                                                                                                      self.cube[0][
                                                                                                                                          column][i],
                                                                                                                                      self.cube[
                                                                                                                                          5][-column-1][-1-i],
                                                                                                                                      self.cube[1][-i-1][column])
                elif direction == 1:  # Twist up
                    self.cube[0][column][i], self.cube[1][-i-1][column], self.cube[3][i][-column-1], self.cube[5][-column-1][-1-i] = (self.cube[1][-i-1][column],
                                                                                                                                      self.cube[
                                                                                                                                          5][-column-1][-1-i],
                                                                                                                                      self.cube[0][
                                                                                                                                          column][i],
                                                                                                                                      self.cube[3][i][-column-1])
                else:
                    print(f'ERROR - direction must be 0 (down) or 1 (up)')
                    return
            # Rotating connected face
            if direction == 0:  # Twist down
                if column == 0:
                    self.cube[4] = [list(x) for x in zip(
                        *reversed(self.cube[4]))]  # Transpose back
                elif column == len(self.cube[0]) - 1:
                    self.cube[2] = [list(x) for x in zip(
                        *reversed(self.cube[2]))]  # Transpose top
            elif direction == 1:  # Twist up
                if column == 0:
                    self.cube[4] = [list(x) for x in zip(
                        *self.cube[4])][::-1]  # Transpose back
                elif column == len(self.cube[0]) - 1:
                    self.cube[2] = [list(x) for x in zip(
                        *self.cube[2])][::-1]  # Transpose top
        else:
            # print error message
            print(
                f'ERROR - desired column outside of rubiks cube range. Please select a column between 0-{len(self.cube[0])-1}')
            return
