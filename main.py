import json
import os.path
import time

from rubix_cube import RubiksCube
from korf_solver import korf, heuristic_db


MAX_MOVES = 5
NEW_HEURISTICS = False
HEURISTIC_FILE = 'heuristic.json'

# --------------------------------
cube = RubiksCube(n=3)
cube.show()
print('--------------------------')
# --------------------------------

if os.path.exists(HEURISTIC_FILE):
    with open(HEURISTIC_FILE) as f:
        h_db = json.load(f)
else:
    h_db = None

start = time.time()
if h_db is None or NEW_HEURISTICS is True:
    actions = [(r, n, d) for r in ['h', 'v', 's']
               for d in [0, 1] for n in range(cube.n)]
    h_db = heuristic_db(
        cube.stringify(),
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
# --------------------------------

cube.shuffle(
   MAX_MOVES
)
cube.show()
print('----------')
# --------------------------------


solver = korf(h_db)
moves = solver.run(cube.stringify())
end = time.time()
print(moves)

for m in moves:
    if m[0] == 'h':
        cube.horizontal_twist(m[1], m[2])
    elif m[0] == 'v':
        cube.vertical_twist(m[1], m[2])
    elif m[0] == 's':
        cube.side_twist(m[1], m[2])
cube.show()
print(end-start)
