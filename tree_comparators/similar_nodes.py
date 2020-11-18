from collections import Counter

from structures.tree import Tree


class NodesQuantityComparator():
    def __init__(self, T1: Tree, T2: Tree):
        self.T1 = T1
        self.T2 = T2


    def compare(self):
        nodes1 = Counter(self.T1.get_nodes())
        nodes2 = Counter(self.T2.get_nodes())
        return sum((nodes1 & nodes2).values())/max(sum(nodes1.values()), sum(nodes2.values())), \
            sum((nodes1 & nodes2).values())/(sum((nodes1 & nodes2).values()) + sum((nodes1 - nodes2).values()) + sum((nodes2 - nodes1).values())) 

