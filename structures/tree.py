from . import node

class Tree():
    def __init__(self, root):
        self.root : node.Node = root
        # self.nodes : [str] = []

    def get_nodes(self):
        
        nodes = []
        def get_children(node):
            for child in node.children:
                nodes.append(child.name)
                get_children(child)
        
        get_children(self.root)
        return nodes

    def get_node_children(self, node):
        nodes = []
        def f(node):
            for child in node.children:
                nodes.append(child)
                f(child)
        f(node)
        # for child in node.children:
        #     nodes.append(child)
        #     self.get_node_children(child)
        return nodes

    def get_nodes_postorder(self):
        nodes = []
        def get_children_post(node):
            for child in node.children:
                get_children_post(child)
            nodes.append(node)
        get_children_post(self.root)
        return nodes