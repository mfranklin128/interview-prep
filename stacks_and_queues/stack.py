import node

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0
        
    def push_list(self, l):
        for data in l:
            self.push(data)

    def push(self, data):
        self.count += 1
        if not self.top:
            self.top = node.Node(data)
        else:
            new_node = node.Node(data)
            new_node.next = self.top
            self.top = new_node
            
    def pop(self):
        if not self.top:
            return None
        self.count -= 1
        data = self.top.data
        self.top = self.top.next
        return data
        
    def peek(self):
        if self.top:
            return self.top.data
        return None
        
    def __len__(self):
        return self.count
