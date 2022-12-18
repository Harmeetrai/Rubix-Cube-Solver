import time
import multiprocessing
import json
import os.path

from rubix_cube import RubiksCube
from korf_solver import korf, heuristic_db

HEURISTIC_FILE = 'heuristic.json'
NEW_HEURISTICS = True

# a dictionary for the time taken to solve the cube
time_taken = {}

# file to store the time taken to solve the cube

# Create an instance of the Rubik's cube class
cube = RubiksCube(n=3)

# Shuffle the cube
cube.shuffle(l_rot=5, u_rot=5)

# Show the cube
cube.show()


def run_korf(cube, max_moves):
    actions = [(r, n, d) for r in ['h', 'v', 's']
               for d in [0, 1] for n in range(cube.n)]
    h_db = None
    h_db = heuristic_db(
        cube.stringify(),
        actions,
        max_moves=max_moves,
        heuristic=h_db
    )
# Create an instance of the korf class
    korfs = korf(h_db)

    # Start timer
    start = time.time()

    # Use the Kociemba algorithm to solve the Rubik's cube
    moves = korfs.run(cube.stringify())

    # End timer
    end = time.time()

    # add time taken to solve the cube to the dictionary
    time_taken[max_moves] = end - start


if __name__ == '__main__':
    # Create a list of processes that we want to run
    processes = [multiprocessing.Process(
        target=run_korf, args=(cube, i)) for i in range(1, 3)]

    # Run processes
    for p in processes:
        p.daemon = True
        p.start()

    print("done")

    # Exit the completed processes
    for p in processes:
        p.join()

    print("done")
