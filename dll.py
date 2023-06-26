class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None       
class DLL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def printf(self):
        pv=self.head
        
        while(pv):
            print(str(pv.data)+"-->")
            #pv2=pv
           # print(pv.prev,pv.next)
            pv=pv.next
            
        print("END")
    def printb(self):
        pv=self.tail
        #print("Rev")
        while(pv):
            print(pv.data)
            pv=pv.prev
        print("END")
    def dele(self):
        pv=self.head
        for i in range(self.size-2):
            pv=pv.next
        #pv.next.prev=None
        pv.next=None
        self.tail=pv
        self.size=self.size-1
    def delb(self):
      #  pv=self.head
        self.head=self.head.next
        self.head.prev=None
        self.size=self.size-1
    def delm(self,pos):
        pv=self.head
        for i in range(pos):
            if i==pos-1:
                break
            pv=pv.next
       
        pv.next.next.prev=pv
        pv.next=pv.next.next
        self.size=self.size-1
    def insertb(self,data):
        NN=Node(data)
        NN.next=self.head
        NN.prev=None
        if self.head!=None:            
            self.head.prev=NN
        self.head=NN
        if self.tail==None:
            self.tail=self.head
        self.size=self.size+1   
    def inserte(self,data):
        NN=Node(data)  
        
        self.tail.next=NN
        NN.prev=self.tail
        self.tail=NN   
        self.size=self.size+1
    def insertm(self,data,pos):
        if pos==0:
            self.insertb(data)
        if pos==self.size-1:
            self.inserte(data)
        NN=Node(data)
        pv=self.head
        for i in range(pos):
            if i==pos-1:
                break
            pv=pv.next 
        NN.prev=pv
        NN.next=pv.next
        pv.next.prev=NN
        pv.next=NN
        if self.tail==None:
            self.tail=self.head
        self.size=self.size+1
    def leng(self):
        print("Length is "+str(self.size))

d=DLL()
d.insertb(3)
d.insertb(6)
d.inserte(5)
d.inserte(25)
d.inserte(32)
d.inserte(9)

d.insertm(2,2)
d.insertm(23, 4)
d.dele()
d.delb()
d.delm(3)
d.printf()
d.printb()
d.leng()
