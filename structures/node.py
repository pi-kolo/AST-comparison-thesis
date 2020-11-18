class Node():
    def __init__(self, name: str):
        self.parent : Node = None
        self.children : [Node] = []
        self.name = name
