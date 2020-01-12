import stack

# 3, 5, 5, 5, 2, 3, 3, 3, 1
# ^           ^           ^

class StackWithMin:
    def __init__(self):
        self.stack = stack.Stack()
        # A stack containing the sizes at which a minimum was seen.
        self.minimum_indices = stack.Stack()
        self.minimums = stack.Stack()
    
    # Convenience method.
    def push_list(self, l):
        for data in l:
            self.push(data)
    
    def push(self, data):
        if len(self.minimums) == 0:
            self.minimums.push(data)
            self.minimum_indices.push(1)
        self.stack.push(data)
        if data < self.minimums.peek():
            self.minimum_indices.push(len(self.stack))
            self.minimums.push(data)
        
    def pop(self):
        if self.stack == None:
            return None
        minimum_size = self.minimum_indices.peek()
        if len(self.stack) == minimum_size:
            self.minimum_indices.pop()
            self.minimums.pop()
        return self.stack.pop()
    
    def stack_minimum(self):
        return self.minimums.peek()
        
stack_with_min = StackWithMin()
stack_with_min.push_list([3, 5, 5, 5, 2, 3, 3, 3, 1])
print(stack_with_min.stack_minimum())
print('pop=%d' % stack_with_min.pop())
print('new min = %d' % stack_with_min.stack_minimum())
print('pop=%d' % stack_with_min.pop())
print('pop=%d' % stack_with_min.pop())
print('pop=%d' % stack_with_min.pop())
print('min=%d' % stack_with_min.stack_minimum())
print('pop=%d' % stack_with_min.pop())
print('min=%d' % stack_with_min.stack_minimum())
print('pop=%d' % stack_with_min.pop())
print('pop=%d' % stack_with_min.pop())
print('pop=%d' % stack_with_min.pop())
print('min=%d' % stack_with_min.stack_minimum())
print('pop=%d' % stack_with_min.pop())
print('min=%s' % stack_with_min.stack_minimum())