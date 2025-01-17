from collections import Counter

from structures.tree import Tree


def node_quantity_compare(T1: Tree, T2: Tree) -> (float, float):
    """ Count nodes of each type and calculate similarity """

    nodes1 = Counter(T1.get_nodes_pre(only_name=True))
    nodes2 = Counter(T2.get_nodes_pre(only_name=True))

    return sum((nodes1 & nodes2).values()) / max(sum(nodes1.values()), sum(nodes2.values()))
