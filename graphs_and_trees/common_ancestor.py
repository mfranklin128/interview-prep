import binary_tree

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
    
def find(root, node):
    if not root:
        return None
    if root == node:
        return [node]
    left_path = find(root.left, node)
    if left_path:
        left_path.append(root)
        return left_path
    right_path = find(root.right, node)
    if right_path:
        right_path.append(root)
        return right_path
    return None

def common_ancestor(root, x, y):
    x_path = find(root, x)
    y_path = find(root, y)
    if not x_path or not y_path:
        return None
    for x_node in x_path:
        for y_node in y_path:
            if x_node == y_node:
                return x_node
    return None # no common ancestor
    
root = make_testdata()
print(common_ancestor(root, root.left.left.left, root.right.right.left).data)
    
    