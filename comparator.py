import sys
import ast
import argparse 

from tree_comparators.metric import TreeMetric
from tree_comparators.similar_nodes import NodesQuantityComparator
from custom_ast import build_tree, print_tree
from tree_comparators.dynamic_ted import tree_edit_distance, printable_distance


def main():
    parser = argparse.ArgumentParser(description="Python codes similarity measurement. When no optional parameter, similarity calculated using all three methods")
    parser.add_argument("file1", help="First python file to be analysed")
    parser.add_argument("file2", help="Second python file to be analysed")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--counting", help="Check similarity by counting the same nodes", action="store_true")
    group.add_argument("-ted", "--tree_edit_distance", help="Check similarity by calculating tree edit distance", action="store_true")
    group.add_argument("-lcf", "--largest_common_forest", help="Check similarity by finding largest common forest", action="store_true")
    args = parser.parse_args()
    
    file1, file2 = args.file1, args.file2
    try:
        with open(file1, encoding="utf-8") as f1:
            try:
                ast_1 = ast.parse(f1.read())
            except SyntaxError as error:
                print(f"Error: File 1 is not correct grammatically. \nLine {error.lineno}, {error.msg}: \n {error.text} ")
                return
        with open(file2, encoding="utf-8") as f2:
            try:
                ast_2 = ast.parse(f2.read())
            except SyntaxError as error:
                print(f"Error: File 2 is not correct grammatically. \nLine{error.lineno}, {error.msg}: \n {error.text} ")
                return
    except FileNotFoundError:
        print("Error: given files do not exist")
        return 

    tree1 = build_tree(ast_1)
    tree2 = build_tree(ast_2)
    
    if args.largest_common_forest:
        metric = TreeMetric(tree1, tree2)
        metric_similarity = metric.count_similarity()
        print(f'Similarity calculated with largest common forest algorithm: {metric_similarity}')
        return
    if args.tree_edit_distance:
        edit_distance = tree_edit_distance(tree1, tree2)
        print(f'Similarity calculated with tree edit distance algorithm: {edit_distance}')
        return
    if args.counting:
        quantity_similarity = NodesQuantityComparator(tree1, tree2).compare()
        print(f'Similarity calculated by counting same nodes: {quantity_similarity}')
        return     
   
    print("Similarity:")
    metric = TreeMetric(tree1, tree2)
    metric_similarity = metric.count_similarity()
    print(f'•calculated with largest common forest algorithm: {metric_similarity}')
    quantity_similarity = NodesQuantityComparator(tree1, tree2).compare()
    print(f'•calculated by counting same nodes: {quantity_similarity}')
    edit_distance = tree_edit_distance(tree1, tree2)
    print(f'•calculated with tree edit distance algorithm: {edit_distance}')

if __name__ == "__main__":
    main()
