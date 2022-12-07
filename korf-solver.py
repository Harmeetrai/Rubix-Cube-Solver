class korf(object):
    def __init__(self, heuristic, depth_max = 20):
        """pass"""
        self.depth_max = depth_max
        self.maxthresh = depth_max
        self.minthresh = None

    # search for the solution