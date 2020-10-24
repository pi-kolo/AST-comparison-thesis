class Node():
    def __init__(self, name):
        self.parent : Node = None
        self.children : [Node] = []
        self.name: str = name
