import ast

from structures.node import Node
from structures.tree import Tree

# build custom AST tree from ast object
def build_tree(ast_root: ast.AST) -> Tree: 
    
    # add all ast_node children to custom_node children list
    def walk_children(custom_node, ast_node) -> None:
        for child in ast.iter_child_nodes(ast_node):
            new_node = Node(type(child).__name__)
            custom_node.children.append(new_node)
            child.parent = custom_node
            walk_children(new_node, child)

    root_node = Node(type(ast_root).__name__)
    tree = Tree(root_node)
    walk_children(root_node, ast_root)
    return tree


def print_tree(tree: Tree) -> None:

    def print_child_nodes(node, level) -> None:
        for child in node.children:
            print(2*level * '-' + child.name)
            print_child_nodes(child, level + 1)

    print(tree.root.name)
    print_child_nodes(tree.root, 1)