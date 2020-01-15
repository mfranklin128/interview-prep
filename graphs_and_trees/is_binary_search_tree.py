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
    
def is_bst_helper(root):
    if not root.left and not root.right:
        return root.data
    left_max = None
    right_max = None
    if root.left:
        left_max = is_bst_helper(root.left)
        if left_max == None or left_max > root.data:
            return None
    if root.right:
        right_max = is_bst_helper(root.right)
        if right_max == None or right_max < root.data:
            return None
    if right_max:
        return right_max
    return root.data
        
    
def is_bst(root):
    return is_bst_helper(root) != None

root = make_testdata()
print(is_bst(root))