import binary_tree
# [6] -> [4, 8] -> [1, ], [6, 9] -> [], 
def make_testdata():
    root = binary_tree.Node(6)
    root.left = binary_tree.Node(4)
    root.left.left = binary_tree.Node(1)
    root.left.left.left = binary_tree.Node(0)
    root.left.left.right = binary_tree.Node(3)
    root.right = binary_tree.Node(8)
    root.right.left = binary_tree.Node(6)
    root.right.right = binary_tree.Node(9)
    root.right.right.left = binary_tree.Node(4)
    root.right.right.right = binary_tree.Node(10)
    return root
    
def is_bst(root):
    if not root:
        return True
    if not root.left and not root.right:
        return True
    if not root.left:
        return root.right.data > root.data and is_bst(root.right)
    if not root.right:
        return root.left.data < root.data and is_bst(root.left)
    return (
        root.left.data < root.data and
        root.right.data > root.data and
        is_bst(root.left) and
        is_bst(root.right)
    )

root = make_testdata()
print(is_bst(root))