from random import choice

import cube as cube
from tqdm import tqdm
from rubix-cube import RubixCube


class korf(object):
    def __init__(self, heuristic, depth_max = 20):
        """pass"""
        self.depth_max = depth_max
        self.maxthresh = depth_max
        self.minthresh = None

    # search for the solution

    def run(self, state):
        while True:
            status = self.search(state,1)
            if status:
                return self.moves
            self.moves = []
            self.thresh = self.minthresh
        return []

    def search(self,state,cost_curr_node):
        rubixcube = RubixCube(state = state)
        if rubixcube.solved():
            return True
        elif len(self.moves) >= self.thresh:
            return False
        min_value = float('inf')
        best_act = None
        for a in [(r,n,d) for r in ['hor_twist','ver_twist','side_twist'] for d in [0,1] for n in range(rubixcube.n)]:
            rubixcube = RubixCube(state = state)
            if a[0] == 'hor_twist':
                rubixcube.horizontal_twist(a[1],a[2])
            if a[0] == 'ver_twist':
                rubixcube.vertical_twist(a[1],a[2])
            if a[0] == 'side_twist':
                rubixcube.side_twist(a[1],a[2])
            if rubixcube.solved():
                self.moves.append(a)
                return True
            rubixcube_str = rubixcube.stringify()
            heuristic_score = self.heuristic[rubixcube_str] if rubixcube_str in self.heuristic else self.depth_max
            final_score = cost_curr_node + heuristic_score
            if final_score < min_value:
                min_value = final_score
                best_act = [(rubixcube_str, a)]
            elif final_score == min_value:
                if best_act is None:
                    best_act = [(rubixcube_str, a)]
                else:
                    best_act.append((rubixcube_str, a))

        if best_act is not None:
            if self.minthresh is None or min_value < self.minthresh:
                self.minthresh = min_value
            next_act = choice(best_act)
            self.moves.append(next_act[1])
            status = self.search(next_act[0], cost_curr_node + min_value)
            if status:
                return status
        return False

def heuristic_db(cur_state, actions, max_moves = 20, heuristic = None):
    if heuristic is None:
        heuristic = {cur_state: 0}
    queue = [(cur_state, 0)]
    num_nodes = sum([len(actions) ** (x + 1) for x in range(max_moves + 1)])
    with tqdm(total = num_nodes, desc = 'HeurDB') as HeurDB:
        while True:
            if not queue:
                break
            s,d = queue.pop()
            if d > max_moves:
                continue
            for a in actions:
                rubixcube = RubixCube(cur_state = s)
                if a[0] == 'hor_twist':
                    rubixcube.horizontal_twist(a[1], a[2])
                if a[0] == 'ver_twist':
                    rubixcube.vertical_twist(a[1], a[2])
                if a[0] == 'side_twist':
                    rubixcube.side_twist(a[1], a[2])
                a_str = rubixcube.stringify()
                if a_str not in heuristic or heuristic[a_str] > d + 1:
                    heuristic[a_str] = d + 1
                queue.append((a_str, d + 1))
                HeurDB.update(1)
    return heuristic