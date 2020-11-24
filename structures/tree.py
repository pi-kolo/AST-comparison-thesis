from .node import Node

class Tree():
    def __init__(self, root: Node):
        self.root = root
        # self.nodes : [str] = []

    def get_nodes(self):
        nodes = []
        def get_children(node):
            for child in node.children:
                nodes.append(child.name)
                get_children(child)
        
        get_children(self.root)
        return nodes

    def depth_calc(self):
        def depth_levels(node, level):
            node.depth = level
            for child in node.children:
                depth_levels(child, level+1)
        depth_levels(self.root, 0)

    def get_nodes_pre(self):
        nodes = []
        def get_children(node):
            for child in node.children:
                nodes.append(child)
                get_children(child)
        nodes.append(self.root)
        get_children(self.root)
        return nodes

    def get_node_children(self, node: Node) -> [Node]:
        nodes = []
        def f(node):
            for child in node.children:
                nodes.append(child)
                f(child)
        f(node)
        return nodes

    def get_nodes_postorder(self):
        nodes = []
        def get_children_post(node):
            for child in node.children:
                get_children_post(child)
            nodes.append(node)
        get_children_post(self.root)
        return nodes