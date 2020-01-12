import stack

def pop_min_val(this_stack):
    dummy_stack = stack.Stack()
    min_val = None
    
    while len(this_stack) > 0:
        val = this_stack.pop()
        if min_val == None or val < min_val:
            min_val = val
        dummy_stack.push(val)
    to_return = None
    while len(dummy_stack) > 0:
        val = dummy_stack.pop()
        if val == min_val and to_return == None:
            to_return = val
        else:
            this_stack.push(val)
    return to_return
        

def sort_stack(unsorted_stack):
    # pop from stack onto dummy stack, find the min value
    # pop back from dummy stack, put the min element on the sorted stack
    # repeat
    sorted_stack = stack.Stack()
    while len(unsorted_stack) > 0:
        sorted_stack.push(pop_min_val(unsorted_stack))
    return sorted_stack
        
test_data = stack.Stack()
test_data.push_list([5, 3, 2, 4, 1])
sorted_test_data = sort_stack(test_data)
while len(sorted_test_data) > 0:
    print(sorted_test_data.pop())