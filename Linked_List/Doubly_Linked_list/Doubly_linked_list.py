class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            cur=self.head
            while cur.next:
                cur=cur.next
            cur.next=new_node
            new_node.prev=cur

    def prepend(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node


    def print_list(self):
        cur=self.head
        while cur:
            print(cur.data)
            cur=cur.next

    def add_after_node(self,key,data):
        cur=self.head
        while cur:
            if cur.next is None and cur.data==key:#list only has one node
                self.append(data)
                return
            elif cur.data==key:
                new_node=Node(data)
                new_node.prev=cur
                new_node.next=cur.next
                cur.next.prev=new_node
                cur.next=new_node
            cur=cur.next

    def add_before_node(self,key,data):
        cur=self.head
        while cur:
            if cur.data==key and cur.prev is None:#first Node
                self.prepend(data)
                return
            elif cur.data ==key:
                new_node=Node(data)
                new_node.prev=cur.prev
                new_node.next=cur
                cur.prev.next=new_node
                cur.prev=new_node
            cur=cur.next

    def delete(self,key):
        cur=self.head
        while cur:
            if cur.data==key and cur.prev is None:#we can either check cur.prev is none OR cur==self.head
                if not cur.next:#only one node is there
                    self.head=None
                    cur.next=cur.prev=None#deleting node
                    cur=None#deleting node
                    return

                else:
                    self.head=cur.next
                    cur.next.prev=None#cur.next.prev means prev pointer of the next node to cur
                    cur.next=cur.prev=None#deleting node
                    cur=None#deleting node
                    return
            elif cur.data ==key:
                    if cur.next:#the node with key is not last node
                        cur.prev.next=cur.next
                        cur.next.prev=cur.prev
                        cur.next=cur.prev=cur=None#deleting node
                        return
                    else:#last node
                        cur.prev.next=None
                        cur.next=cur.prev=cur=None#deleting node
                        return
            cur=cur.next

    def reverse(self):
        cur=self.head
        last=None
        while cur:
            cur.next,cur.prev=cur.prev,cur.next
            #print(cur.next,cur.prev)
            if not cur.prev:
                last=cur
            cur=cur.prev
        self.head=last

    def delete_node(self,cur):
        if cur==self.head:
            self.head=cur.next
            cur.prev=cur.next=cur=None
            return
        elif not cur.next:#last node
            cur.prev.next=None
            cur.prev=cur.next=cur=None
            return
        else:
            cur.prev.next=cur.next
            cur.next.prev=cur.prev
            cur.prev=cur.next=cur=None
            return


    def remove_duplicates(self):
        dup_list=[]
        cur=self.head
        while cur:
            if cur.data in dup_list:
                nxt=cur.next
                self.delete_node(cur)
                cur=nxt
            else:
                dup_list.append(cur.data)
                cur=cur.next


    def pair_with_sum(self,n):
        p=self.head
        q=p.next
        l=[]
        while p:
            q=p.next
            while q:
                #print(p.data,q.data)
                if p.data+q.data==n:
                        l.append([p.data,q.data])
                q=q.next
            p=p.next
        return l


dll=DoublyLinkedList()
dll.append('C')
dll.append('D')
dll.prepend('B')
dll.prepend('A')
#dll.print_list()
#print()
#dll.add_after_node('A','M')
#dll.print_list()
#print()
#dll.add_before_node('C','Z')
#dll.print_list()
#print()
#dll.delete('D')
dll.append('C')
dll.append('A')
dll.append('D')
dll.print_list()
#dll.reverse()
#dll.print_list()
print()
print("Removing Duplicates")
dll.remove_duplicates()
dll.print_list()
print()
dll1=DoublyLinkedList()
dll1.append(1)
dll1.append(2)
dll1.append(3)
dll1.append(4)
dll1.append(5)
dll1.append(6)
print(dll1.pair_with_sum(5))
