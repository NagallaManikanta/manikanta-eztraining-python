'''class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            res=self.head
            while res:
                print(res.data,"->",end=" ")
                res=res.ref
    def add(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
l1=linkedlist()
l1.display()
l1.add(10)
l1.add(20)
l1.display()
l1=linkedlist()
n=node(10)
l1.head=n
n1=node(10)
l1.head.ref=n1
n2=node(11)
n1.ref=n2
n3=node(12)
n2.ref=n3
l1.display()

class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linked:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linked is empty")
        else:
            res=self.head
            while res:
                print(res.data,"->",end=" ")
                res=res.ref
l1=linked()
n=node("w")
l1.head=n
n1=node("i")
n.ref=n1
n2=node("n")
n1.ref=n2
n3=node("n")
n2.ref=n3
n4=node("e")
n3.ref=n4
n5=node("r")
n4.ref=n5
l1.display()
#=================inserting at beginning=======================================
class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            res=self.head
            while res:
                print(res.data,"->",end=" ")
                res=res.ref
    def add(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
l1=linkedlist()
l1.display()
l1.add(10)
l1.add(20)
l1.display()'''
#=============================================
'''class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            res=self.head
            while res:
                print(res.data,"->",end=" ")
                res=res.ref
    def add(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
    def insert_end(self,data):
        new_node=node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
l1=linkedlist()
l1.display()
l1.insert_end(10)
l1.insert_end(20)
l1.insert_end(70)
l1.display() 4

#===============================================
class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("linkedlist is empty")
        else:
            res=self.head
            while res:
                print(res.data,"->",end=" ")
                res=res.ref
    def add(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
    def insert_pos(self,pos,data):
        np=node(data)
        temp=self.head
        for i in range(pos):
            temp=temp.ref
        np.ref=temp.ref
        temp.ref=np
l1=linkedlist()
l1.display()
l1.add(10)
l1.add(20)
l1.add(10)
l1.add(20)
l1.add(10)
l1.add(20)
l1.insert_pos(1,10)
l1.insert_pos(0,670)
l1.insert_pos(6,70)
l1.display()
#================================================='''
class node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        if self.ln is None:
            self.head=node(data)
            self.ln=self.head
        else:
            self.ln.ref=node(data)
            self.ln=self.ln.ref
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=" ")
            current=current.ref  
la=linkedlist()
n=int(input("enter the size"))
for i in range(n):
    data=int(input("enter data"))
    la.append(data)
print("the linked list is",end=" ")
la.display()