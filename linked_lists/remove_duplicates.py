import node

def remove_duplicates(head):
    seen = set()
    prev = None
    curr = head
    while curr:
        if curr.data not in seen:
            seen.add(curr.data)
            prev = curr
            curr = curr.next
        else:
            # Remove the node.
            # Note: this is safe because the head can never be a dupe.
            prev.next = curr.next
            curr = curr.next

test_list = node.make_test_list([1, 2, 3, 4, 1, 5, 2, 2, 2, 3, 2, 4])
remove_duplicates(test_list)
node.print_list(test_list)