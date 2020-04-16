class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=None

    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            new_node.next=new_node
        else:
            cur=self.head
            while cur.next != self.head:
                cur=cur.next
            cur.next=new_node
            new_node.next=self.head

    def prepend(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            new_node.next=new_node
        else:
            cur=self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next=new_node
            new_node.next=self.head
            self.head=new_node

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self,key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            self.head=self.head.next
            cur.next=self.head
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    #cur.next = None error AttributeError: 'NoneType' object has no attribute 'data'
                    cur=cur.next

    def __len__(self):
        count=0
        cur=self.head
        while cur:
            count+=1
            cur=cur.next
            if cur==self.head:
                break
        return count


    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size//2
        count = 0

        prev = None
        cur = self.head

        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while cur.next != self.head:
            split_cllist.append(cur.data)
            cur = cur.next
        split_cllist.append(cur.data)

        self.print_list()
        print("")
        split_cllist.print_list()

    def josephus_problem(self,m):#m--step size
        l=len(self)
        c=1
        cur=self.head
        while l>1:
            if c%m==0:
                print("REMOVED:",cur.data)
                self.remove(cur.data)
            l=len(self)
            c+=1
            #print(l,m)
            cur=cur.next
        self.print_list()


    def is_circular_linked_list(self,input_list):
        cur=input_list.head
        while cur:
            cur=cur.next
            if cur==input_list.head:
                return True
        return False
cll=CircularLinkedList()
cll.append('C')
cll.prepend('B')
cll.append('D')
cll.prepend('A')
cll.append('E')
cll.print_list()
print("\n")
#print("Removing Nodes")
#cll.remove("C")
#cll.remove('A')
#cll.remove('E')
#cll.print_list()
#print(len(cll))
#cll.split_list()
cll.josephus_problem(3)
print("")
cll2=CircularLinkedList()
cll2.append(1)
cll2.append(2)
cll2.append(3)
cll2.append(4)
print(cll.is_circular_linked_list(cll2))
