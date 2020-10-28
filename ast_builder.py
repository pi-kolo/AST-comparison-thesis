import ast
from collections import Counter
from structures.node import Node
from structures.tree import Tree
from tree_comparators.metrics import TreeMetric

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
            print(2*level * '-' + child.name, child.subtree_id, child.size)#, child.marked)
            print_child_nodes(child, level + 1)

    print(tree.root.name, tree.root.subtree_id)
    print_child_nodes(tree.root, 1)

with open("test_code/test3/f1.py", "br") as f:
    tree1 = ast.parse(f.read())

with open("test_code/test3/f2.py", "br") as f:
    tree2 = ast.parse(f.read())

t1 = walk_tree(tree1)
t2 = walk_tree(tree2)
m = TreeMetric(t1, t2)
def compare(tree1: Tree, tree2: Tree):
    nodes1 = Counter(tree1.get_nodes())
    nodes2 = Counter(tree2.get_nodes())

    return sum((nodes1 & nodes2).values())/max(sum(nodes1.values()), sum(nodes2.values()))