import time
from rubix_cube import RubixCube
from korf_solver import korf, heuristic_db

# Create an instance of the korf class
kociemba = korf(heuristic_db)

# Create an instance of the RubixCube class
cube = RubixCube()

# Shuffle the cube
cube.shuffle()

# Test different values of max_moves
for max_moves in range(5, 25):
    # Start timer
    start = time.time()

    # Use the Kociemba algorithm to solve the Rubik's cube
    moves = kociemba.run(cube.stringify(), max_moves)

    # Print the sequence of moves needed to solve the cube
    print(f"max_moves = {max_moves}: moves = {moves}")

    # End timer
    end = time.time()

    # Print elapsed time
    print(f"Elapsed time: {end - start} seconds")
