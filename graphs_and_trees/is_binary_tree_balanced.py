import binary_tree

# 4
# |\
# 2 1
# |\
# 6 1 
# |
# 7
def construct_test_data():
    root = binary_tree.Node(4)
    root.left = binary_tree.Node(2)
    root.left.left = binary_tree.Node(6)
    root.left.left.left = binary_tree.Node(7)
    root.right = binary_tree.Node(1)
    root.left.right = binary_tree.Node(1)
    return root
    
    
def balanced_depth(root):
    if not root:
        return 0
    print(root.data)
    left_depth = balanced_depth(root.left)
    right_depth = balanced_depth(root.right)
    if abs(left_depth - right_depth) > 1:
        return -1
    if left_depth == -1 and right_depth == -1:
        return -1
    return max(left_depth, right_depth) + 1

def is_balanced(root):
    return balanced_depth(root) != -1
        

tree = construct_test_data()
print(is_balanced(tree))