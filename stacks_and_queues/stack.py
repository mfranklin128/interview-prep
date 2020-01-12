import node

class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        if not self.top:
            self.top = node.Node(data)
        else:
            new_node = node.Node(data)
            new_node.next = self.top
            self.top = new_node
            
    def pop(self):
        if not self.top:
            return None
        data = self.top.data
        self.top = self.top.next
        return data
        
    def peek(self):
        if self.top:
            return self.top.data
        return None
