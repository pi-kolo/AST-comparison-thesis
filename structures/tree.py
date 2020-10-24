from . import node

class Tree():
    def __init__(self, root):
        self.root : node.Node = root
        # self.nodes : [str] = []

    def get_nodes(self):
        
        nodes = []
        def get_children(node):
            for children in node.children:
                nodes.append(children.name)
                get_children(children)
        
        get_children(self.root)
        return nodes