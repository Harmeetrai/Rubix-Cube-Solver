import json
import os.path

from rubix_cube import RubixCube
from korf_solver import korf, heuristic_db


MAX_MOVES = 5
NEW_HEURISTICS = False
HEURISTIC_FILE = 'heuristic.json'

h_db = None

rubix_cube = RubixCube(n=3)
rubix_cube.print_cube()

if os.path.exists(HEURISTIC_FILE):
    with open(HEURISTIC_FILE) as f:
        h_db = json.load(f)
else:
    h_db = None

if h_db is None or NEW_HEURISTICS is True:
    actions = [(r, n, d) for r in ['h', 'v', 's']
               for d in [0, 1] for n in range(rubix_cube.n)]
    h_db = heuristic_db(
        rubix_cube.stringify(),
        actions,
        max_moves=MAX_MOVES,
        heuristic=h_db
    )

    with open(HEURISTIC_FILE, 'w', encoding='utf-8') as f:
        json.dump(
            h_db,
            f,
            ensure_ascii=False,
            indent=4
        )
# ---------------------------

# shuffle the cube
rubix_cube.shuffle()

print()
rubix_cube.print_cube()

# solver the cube
solve = korf(h_db)
moves = solve.run(rubix_cube.stringify())
print(moves)

for m in moves:
    if m[0] == 'h':
        rubix_cube.horizontal_twist(m[1], m[2])
    elif m[0] == 'v':
        rubix_cube.vertical_twist(m[1], m[2])
    elif m[0] == 's':
        rubix_cube.side_twist(m[1], m[2])
rubix_cube.print_cube()
# python3 .\main.py
