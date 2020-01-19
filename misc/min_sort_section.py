def min_sort_section(arr):
    if not arr:
        return (0, 0)
    # Look from the beginning and find the first out-of-order index.
    left_val = arr[0]
    left_index = 0
    for index, value in enumerate(arr):
        if value < left_val:
            break
        else:
            left_index = index
            left_val = value
    if left_index == len(arr) - 1:
        return (0, len(arr) - 1)
        
    # Find the smallest thing in the rest of the array.
    minval = left_val
    for index, value in enumerate(arr[left_index:]):
        if value < minval:
            minval = value
    # Find the index where the smallest thing belongs; that's our left bound.
    for index, value in enumerate(arr):
        if value > minval:
            left_index = index
            break
    
    # Repeat the same process, starting on the right.
    right_val = arr[-1]
    right_index = len(arr) - 1
    for i in range(len(arr)):
        index = len(arr) - i - 1
        value = arr[index]
        if value > right_val:
            break
        else:
            right_val = value
            right_index = index
    # Find the biggest thing in the rest of the array.
    maxval = right_val
    for i in range(right_index):
        index = right_index - i - 1
        value = arr[index]
        if value > maxval:
            maxval = value
    # Find the index where the biggest thing belongs; that's our right bound.
    for i in range(len(arr)):
        index = len(arr) - i - 1
        value = arr[index]
        if value < maxval:
            right_index = index
            break
    return (left_index, right_index)
    
l = [1, 2, 4, 7, 10, 11, 7, 17, 6, 7, 16, 18, 19]
print('%d, %d' % (min_sort_section(l)))