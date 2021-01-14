import random


class NodeData(object):
    def __init__(self, key: int, info="", tag=0, weight=1, pos=None):
        self.key = key
        self.info = info
        self.tag = tag
        self.weight = weight
        if pos is not None:
            self.pos = pos
        else:
            self.pos = (random.randint(1, 10), random.randint(1, 10))

    def __repr__(self):
        return "{}".format(self.key)
