"""Implementation os stack"""
class Stack():
	def __init__(self):
		self.items=[]
	def push(self,item):
		self.items.append(item)
	def is_empty(self):
		return self.items==[]
	def pop(self):
		if not self.is_empty():
			return self.items.pop()
		else:
			return("Stach is empty")
	def peek(self):
		if not self.is_empty():
			return self.items[-1]
		else:
			return("Stack is empty")
	def get_stack(self):
		return self.items
"""
s=Stack()
print(s.is_empty())
s.push("A")
s.push("B")
s.push("C")
s.push("D")
s.push("E")
print(s.is_empty())
print(s.get_stack())
z=s.pop()
print(s.get_stack())
"""
