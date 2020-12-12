class Node():
    
    def __init__(self, name: str) -> None:
        self.parent = None
        self.children = []
        self.name = name
