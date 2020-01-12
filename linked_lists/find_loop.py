import node

# a -> b -> c -> d -> e -> c
# a, a
# b, c
# c, e
# d, d
def find_loop(head):
    # Step 1: find a loop point.
    # Step 2: start runner at the beginning of the list.
    #   2a: From the loop point, iterate until:
    #       2a1: you hit the runner from (2). This is your loop start.
    #       2a2: you return to the loop point. 'runner' isn't in your loop.
    #       2a3: Increment runner, back to 2a.
    curr = head
    runner = curr.next
    while curr != runner:
        curr = curr.next
        runner = runner.next.next
    loop_point = curr
    curr = head
    while curr:
        loop_runner = loop_point.next
        while loop_runner != loop_point:
            if loop_runner == curr:
                return curr.data
            loop_runner = loop_runner.next
        if loop_runner == curr:
                return curr.data
        curr = curr.next
    # This should never happen.
    return None
    
test_list = node.make_test_list(['a', 'b', 'c', 'd', 'e'])
# Introduce a loop.
corrupt_dst = test_list.next.next
corrupt_src = test_list.next.next.next.next
assert not corrupt_src.next
corrupt_src.next = corrupt_dst
print(find_loop(test_list))