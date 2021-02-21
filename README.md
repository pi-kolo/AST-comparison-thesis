# AST-comparison-thesis
Engineering thesis - Comparison of source codes by building their syntactic trees

Simple tool for python source codes plagiarism detection.
Used algorithms:
- largest common forest - finds forest of common subtrees of syntax trees
- tree edit distance - finds the shortest sequence of basic operations on trees (insertion, deletion or substitution of a node) that transforms one tree to another
- counting nodes - counts common nodes in both syntax trees

```
usage: comparator.py [-h] [-c | -ted | -lcf] [-n N] file1 file2

Python codes similarity measurement. 
When no optional parameter, similarity calculated using all three methods

positional arguments:
  file1             First python file to be analysed
  file2             Second python file to be analysed

optional arguments:
  -h, --help        show this help message and exit
  -c, --counting    Check similarity by counting the same nodes
  -ted, --tree_edit_distance
                    Check similarity by calculating the tree edit distance
  -lcf, --largest_common_forest
                    Check similarity by finding the largest common forest
  -n N              Minimal size of a subtree, required when -lcf

```
