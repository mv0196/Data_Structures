from Queue import Queue
from stack_implementation import Stack
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self,root):
        self.root=Node(root)

    def print_tree(self,traversal_type):
        if traversal_type=='preorder':
            return self.preorder_print(self.root,"")
        elif traversal_type=='inorder':
            return self.inorder_print(self.root,"")
        elif traversal_type=='postorder':
            return self.postorder_print(self.root,"")
        elif traversal_type=='levelorder':
            return self.levelorder_print(self.root)
        elif traversal_type=='reverselevelorder':
            return self.reverse_levelorder_print(self.root)

        else:
            print("Traversal type: "+str(traversal_type)+" is not supported")
            return False

    def preorder_print(self,start,traversal):#traversal to store result
        """root->left->right"""
        if start:#checking null
            traversal+=(str(start.data)+"-")
            traversal=self.preorder_print(start.left,traversal)
            traversal=self.preorder_print(start.right,traversal)
        return traversal

    def inorder_print(self,start,traversal):
        """"left->root->right"""
        if start:
            traversal=self.inorder_print(start.left,traversal)
            traversal+=(str(start.data)+"-")
            traversal=self.inorder_print(start.right,traversal)
        return traversal

    def postorder_print(self,start,traversal):
        """"left->right->root"""
        if start:
            traversal=self.postorder_print(start.left,traversal)
            traversal=self.postorder_print(start.right,traversal)
            traversal+=(str(start.data)+"-")
        return traversal

    def levelorder_print(self,start):
        if start is None:
            return
        traversal=""
        queue=Queue()
        queue.enqueue(start)
        while len(queue)>0:
            traversal+=str(queue.peek())+"-"
            node=queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal


    def reverse_levelorder_print(self,start):
        if start is None:
            return
        traversal=""
        queue=Queue()
        queue.enqueue(start)
        stack=Stack()
        while len(queue)>0:
            node=queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        while not stack.is_empty():
            traversal+=str(stack.pop().data)+"-"
        return traversal

    def height(self,node):
        if node is None:
            return -1
        left_height=self.height(node.left)
        right_height=self.height(node.right)
        return 1+max(left_height,right_height)

    def size(self):
        if self.root is None:
            return 0
        stack=Stack()
        stack.push(self.root)
        n=1
        while len(stack)>0:
            node=stack.pop()
            if node.left:
                stack.push(node.left)
                n+=1
            if node.right:
                stack.push(node.right)
                n+=1
        return n

    def size_rec(self,node):
        if node is None:
            return 0
        return 1+self.size_rec(node.left)+self.size_rec(node.right)


"""
     1
  2     3
4  5   6  7


"""


tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.right=Node(5)
tree.root.left.left=Node(4)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
#tree.root.right.right.right=Node(8)

#print(tree.print_tree("preorder"))
print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))
print(tree.print_tree("reverselevelorder"))
print("Height:",tree.height(tree.root))
print("Size is:",tree.size())
print("Size using reccursive function is:",tree.size_rec(tree.root))
