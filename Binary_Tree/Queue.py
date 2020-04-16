class Queue:
    def __init__(self):
        self.items=[]
    def enqueue(self,data):
        self.items.insert(0,data)
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items)==0
    def peek(self):
        if not self.is_empty():
            return self.items[-1].data
    def __len__(self):
        return len(self.items)
