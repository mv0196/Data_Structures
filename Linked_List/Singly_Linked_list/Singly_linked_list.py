#video link
#https://www.youtube.com/watch?v=FSsriWQ0qYE&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=5&pbjreload=10
#we will make 2 classes,one for NOde and another for the LinkedList itself
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_list(self):#prints the LinkedList
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next

    def append(self,data):#insert node at the last
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        last_node=self.head#initialised to the head of the list i.e. first node
        while last_node.next:
            last_node=last_node.next
        last_node.next=new_node

    def prepend(self,data):#add node at the begining
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_after_node(self,prev_node,data):#insert node after the given node reffernce
        if not prev_node:
            print("Previous node is not present")
            return
        new_node=Node(data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def insert_after_node_value(self,value,data):#insert node after given node data
        prev_node=self.head
        while prev_node.data!=value:
            prev_node=prev_node.next
        if prev_node.data==value:
            new_node=Node(data)
            new_node.next=prev_node.next
            prev_node.next=new_node
        else:
            print("Previous Node is not in the LinkedList")

    def delete_node(self,key):
        cur_node=self.head
        if cur_node and cur_node.data==key:#i.e. if LinkedList is not empty AND the key is the value of First Node
            self.head=cur_node.next
            cur_node=None
            return
        prev=None
        while cur_node and cur_node.data!=key:
            prev=cur_node
            cur_node=cur_node.next
        if cur_node is None:#means we have reached end of the linkedlist but we dont find the insert_after_node_value
            return
        prev.next=cur_node.next
        cur_node=None

    def delete_node_loc(self,loc):
        cur_node=self.head
        if cur_node and loc==0:
            self.head=cur_node.next
            cur_node=None
            return
        if cur_node and loc>0:
            prev_node=None
            count=0
            while cur_node and count!=loc:
                prev_node=cur_node
                cur_node=cur_node.next
                count+=1
            if cur_node is None:
                return
            prev_node.next=cur_node.next
            cur_node=None
            return
        else:
            return

    def len_iterative(self):
        cur_node=self.head
        count=0
        while cur_node:
            cur_node=cur_node.next
            count+=1
        return count

    def len_reccursive(self,node):
        if node is None:
            return 0
        return 1+self.len_reccursive(node.next)

    def node_swap(self,key1,key2):
        if key1==key2:
            return
        prev1=None
        curr1=self.head
        while curr1 and curr1.data!=key1:
            prev1=curr1
            curr1=curr1.next

        prev2=None
        curr2=self.head
        while curr2 and curr2.data!=key2:
            prev2=curr2
            curr2=curr2.next

        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next=curr2
        else:
            self.head=curr2

        if prev2:
            prev2.next=curr1
        else:
            self.head=curr1

        curr1.next,curr2.next=curr2.next,curr1.next

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.data)

    def reverse_iterative(self):

        prev = None
        cur = self.head
        while cur:#at 7:00  https://www.youtube.com/watch?v=xFuJI29BiDY&list=PL5tcWHG-UPH112e7AN7C-fwDVPVrt0wpV&index=10
            nxt = cur.next
            cur.next = prev

            #self.print_helper(prev, "PREV")
            #self.print_helper(cur, "CUR")
            #self.print_helper(nxt, "NXT")
            #print("\n")

            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev

            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge(self,l2):
        l3=LinkedList()
        cur1=self.head
        cur2=l2.head
        #to check if both LL exists or only ll1 exists or only ll2 exists or none of them exists
        if not cur1:
            return l2
        if not cur2:
            return self
            '''
        if cur1 and cur2:
            pass
        elif cur1:
            l3.head=cur1.head
            return l3
        elif cur2:
            l3.head=cur2.head
            return l3
        else:
            return
            '''
        if cur1.data<=cur2.data:
            l3.head=cur1
            cur1=cur1.next
        else:
            l3.head=cur2
            cur2=cur2.next

        new=l3.head
        while cur1 or cur2:
            if cur1 and cur2:
                if cur1.data<=cur2.data:
                    new.next=cur1
                    new=new.next
                    cur1=cur1.next
                else:
                    new.next=cur2
                    new=new.next
                    cur2=cur2.next
            elif cur1:
                new.next=cur1
                new=new.next
                cur1=cur1.next
            else:
                new.next=cur2
                new=new.next
                cur2=cur2.next
        return l3

    def remove_duplicates(self):
        cur=self.head
        prev=None
        dup_values={}#a dictionary which stores the node value that is encountered once
        while cur:
            if cur.data in dup_values:
                #the node data is duplicate
                #remove node
                prev.next=cur.next
                cur=None
            else:
                #node data is encountered for the first time
                dup_values[cur.data]=1
                prev=cur
            cur=prev.next

    def print_nth_node_from_last(self,n):
        #method 1
        total_length=self.len_iterative()
        cur=self.head
        while cur:
            if total_length==n:
                print(str(n)+"th element from last is:",cur.data)
                return cur
            total_length-=1
            cur=cur.next
        if cur is None:
            return
        '''
        #method 2  more efficient
        p=self.head
        q=self.head
        count=0
        while q and count<n:
            q=q.next
            count+=1
        if not q:
            print(str(n)+"is greater than the length of the linkedlist")
            return
        while p and q:
            p=p.next
            q=q.next
        print(p.data)
        return p

        '''

    def count_occurence(self,n):
        curr=self.head
        occ_values={}
        while curr:
            if curr.data in occ_values:
                occ_values[curr.data]+=1
            else:
                occ_values[curr.data]=1
            curr=curr.next

        #print(occ_values)#to see occurence of all elements
        if n in occ_values:
            return occ_values[n]
        else:
            return "element is not present"

    def count_occurences_recursive(self, node, data):
        if not node:
            return 0
        if node.data == data:
            return 1 + self.count_occurences_recursive(node.next, data)
        else:
            return self.count_occurences_recursive(node.next, data)

    def rotate(self,k):
        p=self.head
        q=self.head
        count=0
        while q.next:
            if count<k-1:
                p=p.next
            count+=1
            q=q.next
        q.next=self.head
        self.head=p.next
        p.next=None

    def is_palindrome(self):
        s=""
        p=self.head
        while p:
            s+=str(p.data)
            p=p.next
        return s==s[::-1]


    def move_head_to_tail(self):
        last=self.head
        prev=None
        while last.next:
            prev=last
            last=last.next
        temp=self.head
        self.head=prev.next
        prev.next=None
        last.next=temp


    def sum_two_lists(self,ll2):
        self.reverse_iterative()
        ll2.reverse_iterative()
        cura=self.head
        curb=ll2.head
        ll3=LinkedList()
        carry=0
        while cura or curb:
            if cura and curb:
                s=cura.data+curb.data+carry
                rem=s%10
                carry=s//10
                print("1",cura.data,curb.data,s,rem,carry)
                ll3.append(rem)
                cura=cura.next
                curb=curb.next
                #print(cura.data,curb.data)
            elif cura:
                s=cura.data+carry
                rem=s%10
                carry=s//10
                print("2",cura.data,curb.data,s,rem,carry)
                ll3.append(rem)
                cura=cura.next
            else:
                s=curb.data+carry
                rem=s%10
                carry=s//10
                print("3",cura.data,curb.data,s,rem,carry)
                ll3.append(rem)
                curb=curb.next
        return ll3

""""------------------------------------------------------------------------------------------------------------------------------------------------------------"""
def string_to_linkedlist(s):
    ll=LinkedList()
    for i in s:
        ll.append(i)
    return ll




ll=LinkedList()
ll.append("A")
ll.append("B")
ll.append("C")
ll.append("D")
'''ll.print_list()
print("------------")
ll.prepend("M")
ll.insert_after_node(ll.head.next.next,"Z")
ll.print_list()
print("------------")
ll.insert_after_node_value("B","Q")
ll.print_list()
print("------------")
ll.delete_node("C")
ll.print_list()
print("------------")
ll.delete_node_loc(1)
ll.print_list()
print("------------")
print(ll.len_iterative())
print("------------")
print(ll.len_reccursive(ll.head))
ll.node_swap('B','A')'''
ll.reverse_iterative()
ll.print_list()
print("=================")
ll1=LinkedList()
ll1.append(1)
ll1.append(5)
ll1.append(7)
ll1.append(7)
ll1.append(9)
#ll1.append(10)

ll2=LinkedList()
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(6)
ll2.append(8)
'''
ll3=ll1.merge(ll2)
ll3.print_list()
ll3.remove_duplicates()
print("After removing duplicates")
ll3.print_list()
nth_last=ll3.print_nth_node_from_last(2)
ll3.append(11)
ll3.append(12)
ll3.append(13)
ll3.append(14)
ll3.append(15)
print("=========")
ll3.print_list()
print("=========")
print(ll3.count_occurence(7))
print(ll3.count_occurences_recursive(ll3.head,7))
print("==========")
ll3.rotate(4)
print("After rotation")
ll3.print_list()
print("++++++++")
ll4=LinkedList()
ll4.append("R")
ll4.append("A")
ll4.append("C")
ll4.append("E")
ll4.append("C")
ll4.append("A")
ll4.append("R")
ll4.print_list()
print("IS_PALINDROME:",ll4.is_palindrome())
print("===============")
string_to_linkedlist("MUKUL").print_list()
print("++++++++++++")
ll3.print_list()
ll3.move_head_to_tail()
print("Moving tail to head")
ll3.print_list()
'''
ll1.print_list()
print("")
ll2.print_list()
ll7=ll1.sum_two_lists(ll2)
ll7.print_list()
