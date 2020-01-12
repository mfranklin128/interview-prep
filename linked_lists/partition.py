import node

def partition(head, x):
    left_side = None
    right_side = None
    curr = head
    while curr:
        if curr.data < x:
            if not left_side:
                left_side = node.Node(curr.data)
            else:
                node.append(left_side, curr.data)
        else:
            if not right_side:
                right_side = node.Node(curr.data)
            else:
                node.append(right_side, curr.data)
        curr = curr.next
    left_side_end = left_side
    while left_side_end.next:
        left_side_end = left_side_end.next
    left_side_end.next = right_side
    return left_side
    
test_list = node.make_test_list([6, 5, 4, 3, 2, 1])
partitioned = partition(test_list, 4)
node.print_list(partitioned)