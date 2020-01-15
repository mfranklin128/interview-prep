import binary_tree
# [6] -> [4, 8] -> [1, ], [6, 9] -> [], 
def make_testdata():
    root = binary_tree.Node(6)
    root.left = binary_tree.Node(4)
    root.left.left = binary_tree.Node(1)
    root.left.left.left = binary_tree.Node(0)
    root.left.left.right = binary_tree.Node(3)
    root.right = binary_tree.Node(8)
    root.right.left = binary_tree.Node(7)
    root.right.right = binary_tree.Node(12)
    root.right.right.left = binary_tree.Node(9)
    root.right.right.right = binary_tree.Node(11)
    return root
    
def is_bst_helper(root, min, max):
    if root == None:
        # Base case.
        return True
    if root.left == None and root.right == None:
        # No children, inherently a BST.
        return (
            (min == None or root.data >= min) and
            (max == None or root.data < max)
            )
    if min == None and max == None:
        # Top of the tree.
        return (
            is_bst_helper(root.left, None, root.data) and
            is_bst_helper(root.right, root.data, None)
        )
    elif min == None:
        return (
            root.data < max and
            is_bst_helper(root.left, None, root.data) and
            is_bst_helper(root.right, root.data, max)
        )
    elif max == None:
        return (
            root.data >= min and
            is_bst_helper(root.left, min, root.data) and
            is_bst_helper(root.right, root.data, None)
        )
    return (
        root.data >= min and root.data < max and
        is_bst_helper(root.left, min, root.data) and
        is_bst_helper(root.right, root.data, max)
        )
    
def is_bst(root):
    return is_bst_helper(root, None, None)

root = make_testdata()
print(is_bst(root))