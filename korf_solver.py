from random import choice

from tqdm import tqdm
from rubix_cube import RubiksCube

# Class to implement Korf's algorithm for solving Rubik's cube


class korf(object):
    # Initialize the class with the heuristic function and the maximum depth for the search
    def __init__(self, heuristic, max_depth=20):
        self.max_depth = max_depth
        self.threshold = max_depth
        self.min_threshold = None
        self.heuristic = heuristic
        self.moves = []

    # Run the search algorithm to find a solution for the given state of the Rubik's cube
    def run(self, state):
        while True:
            status = self.search(state, 1)
            if status:
                return self.moves
            self.moves = []
            self.threshold = self.min_threshold
        return []

    # Recursive search function to find a solution to the Rubik's cube problem
    def search(self, state, g_score):
        # Create a Rubik's cube object from the given state
        cube = RubiksCube(state=state)
        # Check if the cube is solved
        if cube.solved():
            return True
        # Check if the maximum depth has been reached
        elif len(self.moves) >= self.threshold:
            return False
        min_val = float('inf')
        best_action = None
        # Iterate through all possible actions
        for a in [(r, n, d) for r in ['h', 'v', 's'] for d in [0, 1] for n in range(cube.n)]:
            cube = RubiksCube(state=state)
            # Perform the action on the cube
            if a[0] == 'h':
                cube.horizontal_twist(a[1], a[2])
            elif a[0] == 'v':
                cube.vertical_twist(a[1], a[2])
            elif a[0] == 's':
                cube.side_twist(a[1], a[2])
            # Check if the cube is solved after the action
            if cube.solved():
                self.moves.append(a)
                return True
            # Get the string representation of the state of the cube after the action
            cube_str = cube.stringify()
            # Get the heuristic value for the state from the heuristic database
            h_score = self.heuristic[cube_str] if cube_str in self.heuristic else self.max_depth
            # Calculate the f-score for the action
            f_score = g_score + h_score
            # Update the best action and the minimum f-score if necessary
            if f_score < min_val:
                min_val = f_score
                best_action = [(cube_str, a)]
            elif f_score == min_val:
                if best_action is None:
                    best_action = [(cube_str, a)]
                else:
                    best_action.append((cube_str, a))
        if best_action is not None:
            if self.min_threshold is None or min_val < self.min_threshold:
                self.min_threshold = min_val
            next_action = choice(best_action)
            self.moves.append(next_action[1])
            status = self.search(next_action[0], g_score + min_val)
            if status:
                return status
        return False

# Function to generate the heuristic database for the given state of the Rubik's cube


def heuristic_db(state, actions, max_moves=20, heuristic=None):
    if heuristic is None:
        heuristic = {state: 0}
    que = [(state, 0)]
    node_count = sum([len(actions) ** (x + 1) for x in range(max_moves + 1)])
    with tqdm(total=node_count, desc='Heur DB') as pbar:
        while True:
            if not que:
                break
            s, d = que.pop()
            if d > max_moves:
                continue
            for a in actions:
                cube = RubiksCube(state=s)
                if a[0] == 'h':
                    cube.horizontal_twist(a[1], a[2])
                elif a[0] == 'v':
                    cube.vertical_twist(a[1], a[2])
                elif a[0] == 's':
                    cube.side_twist(a[1], a[2])
                a_str = cube.stringify()
                if a_str not in heuristic or heuristic[a_str] > d + 1:
                    heuristic[a_str] = d + 1
                que.append((a_str, d+1))
                pbar.update(1)
    return heuristic
