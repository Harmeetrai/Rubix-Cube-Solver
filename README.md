# Korf's Algorithm for Solving Rubik's Cubes
This project implements Korf's algorithm for solving Rubik's cubes. The algorithm uses a combination of search and heuristics to find the optimal solution for a given Rubik's cube configuration.

## Requirements
- Python 3
- `rubix_cube.py` and `korf_solver.py` from this repository
- The `tqdm` library (can be installed using `pip install tqdm`)

## Usage
To use the solver, run the script `run_solver.py`. The following variables can be modified in the script:

- `MAX_MOVES`: The maximum number of moves used to shuffle the cube.
- `NEW_HEURISTICS`: Set to True to generate new heuristics, set to False to use existing heuristics stored in `HEURISTIC_FILE`.
- `HEURISTIC_FILE`: The file to store/load the heuristics from.

The script will first shuffle the Rubik's cube using a specified number of moves, and then use Korf's algorithm to find the optimal solution. The resulting solution will be printed to the console, and the solved Rubik's cube will be displayed. The time taken to solve the cube will also be printed to the console.

## Customization
The `korf` class in `korf_solver.py` can be modified to customize the behavior of the algorithm. The `max_depth` parameter in the constructor can be adjusted to change the maximum depth of the search tree. The heuristic parameter can be changed to use a different heuristic function.

## Heuristics
The `heuristic_db` function in `korf_solver.py` generates a heuristic database for a given set of actions. This database stores the minimum number of moves required to solve the Rubik's cube from a given configuration. The `max_moves` parameter specifies the maximum depth to search for solutions. The heuristic parameter can be used to provide an existing heuristic database, which will be updated with new values if necessary.

## Notes
- The Rubik's cube is represented as a list of lists of lists, with the outermost list representing the sides of the cube (in the order: up, left, front, right, back, down). The middle list represents the rows on each side, and the innermost list represents the individual tiles on each row.
- The `horizontal_twist` and `vertical_twist` functions in `rubix_cube.py` twist the rows or columns of the Rubik's cube, respectively. The `side_twist` function twists the entire side of the Rubik's cube. The n parameter specifies which row/column/side to twist, and the direction parameter specifies the direction of the twist (0 for clockwise, 1 for counterclockwise).
- The show function in `rubix_cube.py` displays the current state of the Rubik's cube. The stringify function returns a string representation of the current state of the Rubik's cube.
- The reset function in `rubix_cube.py` resets the Rubik's cube to its solved state. The solved function returns a boolean indicating whether the Rubik's