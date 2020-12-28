import os, sys
import ast
import time

from tree_comparators.largest_forest import LargestForest
from tree_comparators.similar_nodes import node_quantity_compare
from custom_ast import build_tree, print_tree
from tree_comparators.dynamic_ted import tree_edit_distance


start = time.time()
path = sys.argv[1]
files = [file for file in os.listdir(path)]
for i, file1 in enumerate(files):
    for i2, file2 in enumerate(files):
        if i2 > i:
            with open(os.path.join(path, file1), encoding='utf-8') as f1, open(os.path.join(path, file2), encoding='utf-8') as f2:
                ast_1, ast_2 = ast.parse(f1.read()), ast.parse(f2.read())
                tree1, tree2 = build_tree(ast_1), build_tree(ast_2)
                metric = LargestForest(tree1, tree2)
                metric_similarity = metric.count_similarity(1)
                metric_similarity_2 = metric.count_similarity(2)
                metric_similarity_3 = metric.count_similarity(3)
                metric_similarity_4 = metric.count_similarity(4)
                quantity_similarity = node_quantity_compare(tree1, tree2)
                edit_distance = tree_edit_distance(tree1, tree2)
                print(f'{file1}; {file2}; {tree1.root.size}; {tree2.root.size}; {quantity_similarity}; {edit_distance}; {metric_similarity}; {metric_similarity_2}; {metric_similarity_3}; {metric_similarity_4}')
print(time.time() - start)