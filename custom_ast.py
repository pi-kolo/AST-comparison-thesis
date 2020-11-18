import ast

from structures.node import Node
from structures.tree import Tree

class CustomAST():
    def __init__(self, ast_tree: ast.AST):
        self.original_ast = ast_tree
        self.tree = self.build_tree()

    # build custom AST tree from ast object
    def build_tree(self):
        
        # add all ast_node children to custom_node children list
        def walk_children(custom_node, ast_node):
            for child in ast.iter_child_nodes(ast_node):
                custom_node.children.append(Node(type(child).__name__))
                walk_children(custom_node.children[-1], child)

        custom_node = Node(type(self.original_ast).__name__)
        tree = Tree(custom_node)
        walk_children(custom_node, self.original_ast)
        return tree


    def print_tree(self):

        def print_child_nodes(node, level):
            for child in node.children:
                print(2*level * '-' + child.name)#, child.subtree_id, child.size)#, child.marked)
                print_child_nodes(child, level + 1)

        print(self.tree.root.name)#, self.custom_tree.root.subtree_id)
        print_child_nodes(self.tree.root, 1)