
class NodeData(object):
    def __init__(self, key: int, info="", tag=0, weight=1, pos=None):
        self.key = key
        self.info = info
        self.tag = tag
        self.weight = weight
        if pos is not None:
            self.position = pos
        else:
            self.position = None

    def __repr__(self):
        return "{}".format(self.key)