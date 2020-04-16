from Queue import Queue
class Node:
    def __init__(self,data=None):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._insert(data,self.root)
    def _insert(self,data,cur_node):#Helper Function for Insertion
        if data<cur_node.data:
            if cur_node.left is None:
                cur_node.left=Node(data)
            else:
                self._insert(data,cur_node.left)
        elif data>cur_node.data:
            if cur_node.right is None:
                cur_node.right=Node(data)
            else:
                self._insert(data,cur_node.right)
        else:#Duplicate Data
            print("Value already exists in tree.")


    def find(self,data):
        if self.root:
            is_found=self._find(data,self.root)
            if is_found:
                return True
            else:
                return False
        else:#Empty Tree
            return None
    def _find(self,data,cur_node):
        if cur_node:
            if cur_node.data==data:
                return True
            elif data<cur_node.data:
                return self._find(data,cur_node.left)
            elif data>cur_node.data:
                return self._find(data,cur_node.right)
        else:
            return False

    def is_bst_satisfied(self):
        def helper(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True

            val = node.data
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(self.root)


    def delete(self,data):
        #print("=-=-=-",data,self.root.data)
        if self.root.data==data:
            if self.root.right:
                min_right=self.minimum(self.root.right,float("inf"))
                self.root.data=min_right
                self._delete(min_right,self.root.right)
                return
            elif self.root.left:
                min_left=self.minimum(self.root.left,float("inf"))
                self.root.data=min_left
                self._delete(min_left,self.root.left)
                return
            else:
                self.root=None
                return
        self._delete(data,self.root)

    def _delete(self,data,cur_node):
        #print("++++",cur_node.data)
        del_node_parent=self.find_node_parent(data,self.root)
        #print("----",del_node_parent,data,cur_node)
        if del_node_parent:
            if del_node_parent.left:
                if del_node_parent.left.data==data:
                    del_node=del_node_parent.left
                    #Case 1 No child
                    if del_node.left is None and del_node.right is None:
                        del_node_parent.left=None
                        del_node=None
                        return
                    #Case 2 only one child
                    #only child is right child
                    elif del_node.left is None and del_node.right:
                        del_node_parent.left=del_node.right
                        del_node.right=del_node=None
                        return
                    #only child is left child
                    elif del_node.right is None and del_node.left:
                        del_node_parent.left=del_node.left
                        del_node.left=del_node=None
                        return
                    #case 3 Node has both child
                    elif del_node.right and del_node.left:
                        min_right=self.minimum(del_node.right,float("inf"))
                        del_node.data=min_right
                        self._delete(min_right,del_node.right)
                        return
            if del_node_parent.right:
                if del_node_parent.right.data==data:
                    del_node=del_node_parent.right
                    #Case 1 No child
                    if del_node.left is None and del_node.right is None:
                        del_node_parent.right=None
                        del_node=None
                        return
                    #Case 2 only one child
                    #only child is right child
                    elif del_node.left is None and del_node.right:
                        del_node_parent.right=del_node.right
                        del_node.right=del_node=None
                        return
                    #only child is left child
                    elif del_node.right is None and del_node.left:
                        del_node_parent.right=del_node.left
                        del_node.left=del_node=None
                        return
                    #case 3 Node has both child
                    elif del_node.right and del_node.left:
                        min_right=self.minimum(del_node.right,float("inf"))
                        del_node.data=min_right
                        self._delete(min_right,del_node.right)
                        return

    def minimum(self,cur_node,mn):#mn= minimum value
        if cur_node:
            mn=min(mn,self.minimum(cur_node.left,mn))
            mn=min(mn,cur_node.data)
            mn=min(mn,self.minimum(cur_node.right,mn))
        return mn

    def find_node_parent(self,data,cur_node):
        if cur_node.left:
            if cur_node.left.data==data:
                return cur_node
            elif data<cur_node.left.data:
                return self.find_node_parent(data,cur_node.left)
            elif data>cur_node.left.data:
                return self.find_node_parent(data,cur_node.right)
        elif cur_node.right:
            if cur_node.right.data==data:
                return cur_node
            elif data<cur_node.right.data:
                return self.find_node_parent(data,cur_node.left)
            elif data>cur_node.right.data:
                return self.find_node_parent(data,cur_node.right)
        else:
            return False

    def print_tree(self):
        if self.root is None:
            print("Tree is Empty")
            return
        q=Queue()
        q.enqueue(self.root)
        while len(q)>0:
            node=q.dequeue()
            print(node.data)
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)


    def __len__(self):
        q=Queue()
        q.enqueue(self.root)
        c=0
        while len(q)>0:
            node=q.dequeue()
            c+=1
            if node.left:
                q.enqueue(node.left)
            if node.right:
                q.enqueue(node.right)
        return c








bst=BST()
bst.insert(4)
bst.insert(2)
bst.insert(1)
bst.insert(8)
bst.insert(5)
bst.insert(10)
print(bst.find(17))
print(bst.is_bst_satisfied())
print("")
tree = BST()
tree.root = Node(1)#HardCoding root to make a False case for checking BST property
tree.root.left = Node(-4)
tree.root.right = Node(3)
tree.root.left.left = Node(-5)
tree.root.left.right = Node(0)
tree.root.right.left = Node(2)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(-8)

#print(bst.is_bst_satisfied())
print(tree.is_bst_satisfied())
print(bst.minimum(bst.root,float("inf")))
print("")
bst.print_tree()
print("")
print("Deleting 1")
bst.delete(1)
bst.print_tree()
print("Deleting 4")
bst.delete(4)
bst.print_tree()
print("Deleting 2")
bst.delete(2)
bst.print_tree()
print("Deleting 8")
bst.delete(8)
bst.print_tree()
print("Deleting 5")
bst.delete(5)
bst.print_tree()
print("Deleting 10")
bst.delete(10)
bst.print_tree()
