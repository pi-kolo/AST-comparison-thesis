class Node():
    """A class representing a simple node of a tree

    Attributes:
        parent: Node object representing parent in a tree 
        children: list of node objects that are direct descendants in a tree
        name: string identifier of a node
    """

    def __init__(self, name: str) -> None:
        self.parent: Node = None
        self.children: [Node] = []
        self.name = name
