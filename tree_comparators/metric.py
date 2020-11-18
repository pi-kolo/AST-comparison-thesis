from collections import deque

from structures.tree import Tree


class TreeMetric():
    def __init__(self, T1: Tree, T2: Tree):
        self.T1 = T1
        self.T2 = T2

    
    def count_certificates(self):
        subtrees = {}
        count = 0
        T1_nodes_post = self.T1.get_nodes_postorder()
        T2_nodes_post = self.T2.get_nodes_postorder()
        for node in T1_nodes_post + T2_nodes_post:
            # node.size = 1
            # print(node.name)
            if len(node.children) > 0:
                subtree_id = (node.name, tuple(child.subtree_id for child in node.children))
            else:
                subtree_id = (node.name, None)
            if subtree_id in subtrees:
                node.subtree_id = subtrees[subtree_id]
            else:
                subtrees[subtree_id] = count
                node.subtree_id = count
                count += 1
            node.size = sum(child.size for child in node.children) + 1

    def largest_common_forest(self):
        L1 = self.T1.get_nodes_postorder()
        L1.sort(key=lambda node: node.subtree_id)
        L2 = self.T2.get_nodes_postorder()
        L2.sort(key=lambda node: node.subtree_id)

        max_size = max(len(L1), len(L2))

        for node in self.T1.get_nodes_postorder() + self.T2.get_nodes_postorder():
            node.marked = False
        v = L1.pop()
        w = L2.pop()
        common = 0

        while len(L1) > 0 and len(L2) > 0:
            if v.marked or v.subtree_id > w.subtree_id:
                v = L1.pop()
            elif w.marked or v.subtree_id < w.subtree_id:
                w = L2.pop()
            else:
                common += v.size
                v.marked = True
                for node in self.T1.get_node_children(v):
                    node.marked = True
                v = L1.pop()
                w.marked = True
                for node in self.T2.get_node_children(w):
                    node.marked = True
                w = L2.pop()
            # print(list(map(lambda x: (x.name, x.marked), self.T1.get_nodes_postorder())))
        return common, max_size
        
    def count_similarity(self):
        self.count_certificates()
        common, max_size = self.largest_common_forest()
        return common / max_size 