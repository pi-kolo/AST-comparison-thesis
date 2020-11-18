import sys
import ast

from tree_comparators.metric import TreeMetric
from tree_comparators.similar_nodes import NodesQuantityComparator
from custom_ast import CustomAST


# Check: Similarity = 2 x S / (2 x S + L + R)


def main():
    if len(sys.argv) != 3:
        print("Dwa pliki źródłowe")
        return
    file1, file2 = sys.argv[1], sys.argv[2]
    with open(file1, "r") as f1, open(file2, "r") as f2:
        ast_1, ast_2 = ast.parse(f1.read()), ast.parse(f2.read())

    tree1 = CustomAST(ast_1)
    tree2 = CustomAST(ast_2)
    
    metric = TreeMetric(tree1.tree, tree2.tree)
    metric_similarity = metric.count_similarity()
    quantity_similarity = NodesQuantityComparator(tree1.tree, tree2.tree).compare()
    print("Podobieństwo:")
    print(f'-przy metryce: {metric_similarity}')
    print(f'-przy zliczaniu: {quantity_similarity}')

    # tree1.print_tree()


if __name__ == "__main__":
    main()
