import node

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enqueue(self, data):
        if not self.head:
            new_node = node.Node(data)
            self.head = new_node
            self.tail = new_node
        else:
            new_node = node.Node(data)
            self.tail.next = new_node
            self.tail = new_node
    
    def dequeue(self):
        if not self.head:
            return None
        data = self.head.data
        self.head = self.head.next
        return data