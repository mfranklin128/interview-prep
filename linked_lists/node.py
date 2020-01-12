class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def append(head, data):
    if not head:
        return Node(data)
    curr = head
    while curr.next:
        curr = curr.next
    new_node = Node(data)
    curr.next = new_node
    return head
    
def make_test_list(l):
    head = None
    for element in l:
        head = append(head, element)
    return head
    
def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=' ')
        curr = curr.next
    print()