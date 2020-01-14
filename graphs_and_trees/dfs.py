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
    
def inorder(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            print(curr.data)
            curr = curr.right
            
def preorder(root):
    if not root:
        return
    stack = []
    stack.append(root)
    while stack:
        curr = stack.pop()
        print(curr.data)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
            
def postorder(root):
    stack = []
    last_visited = None
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            peek = stack[-1]
            if peek.right and peek.right != last_visited:
                curr = peek.right
            else:
                print(peek.data)
                last_visited = stack.pop()
            
root = make_testdata()
print("inorder:")
inorder(root)
print("preorder:")
preorder(root)
print("postorder:")
postorder(root)