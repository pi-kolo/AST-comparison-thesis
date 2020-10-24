import ast
from collections import Counter
from structures.node import Node
from structures.tree import Tree

# ast_node <- from ast.AST
# my_node <- from my tree

def walk_tree(tree_root):

    def walk_children(my_node, ast_node):
        for child in ast.iter_child_nodes(ast_node):
            my_child_node = Node(type(child).__name__)
            my_node.children.append(my_child_node)
            # if isinstance(child, ast.AST):
            walk_children(my_node.children[-1], child)

    my_node = Node(type(tree_root).__name__)
    tree = Tree(my_node)
    walk_children(my_node, tree_root)
    return tree

def print_tree(tree):

    def print_child_nodes(node, level):
        for child in node.children:
            print(2*level * '-' + child.name)
            print_child_nodes(child, level + 1)

    print(tree.root.name)
    print_child_nodes(tree.root, 1)

with open("test_code/test2/lbg.py", "br") as f:
    tree1 = ast.parse(f.read())

with open("test_code/test2/lbg2.py", "br") as f:
    tree2 = ast.parse(f.read())


def compare(tree1: Tree, tree2: Tree):
    nodes1 = Counter(tree1.get_nodes())
    nodes2 = Counter(tree2.get_nodes())

    return sum((nodes1 & nodes2).values()), sum(nodes1.values()), sum(nodes2.values())