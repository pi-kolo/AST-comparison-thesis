from .node import Node

class Tree():
    """ A class representing a tree structure

    Attribiutes:
        root: Node object representing a root of a tree
    """

    def __init__(self, root: Node) -> None:
        self.root = root

    def depth_calc(self) -> None:
        """ Traverses tree and calculates depth of each node """
        def depth_levels(node: Node, level: int) -> None:
            node.depth = level
            for child in node.children:
                depth_levels(child, level + 1)
        depth_levels(self.root, 0)

    def get_nodes_pre(self, only_name: bool):
        """ Traverses tree and returns a list of nodes in preorder
            if only_name then list of strings, else list od node objects
        """

        nodes = []
        def get_children(node):
            for child in node.children:
                nodes.append(child.name if only_name else child)
                get_children(child)
        nodes.append(self.root.name if only_name else self.root)
        get_children(self.root)
        return nodes

    def get_nodes_postorder(self, only_name: bool) -> [Node]:
        """ Traverses tree and returns a list of nodes in preorder
            if only_name then list of strings, else list od node objects
        """
        
        nodes = []
        def get_children(node):
            for child in node.children:
                get_children(child)
            nodes.append(node.name if only_name else node)
        get_children(self.root)
        return nodes

    def get_descendants(self, node: Node) -> [Node]:
        """ Traverses a subtree rooted in a node,
            returns list of node descendants
        """

        nodes = []
        def f(node):
            for child in node.children:
                nodes.append(child)
                f(child)
        f(node)
        return nodes


