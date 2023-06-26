# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 17:20:11 2023

@author: janib
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LL:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def printf(self):
        pv=self.head 
        while(pv):
            print(pv.data)
            pv=pv.next
        print("END")
    def insertb(self,data):
        NN=Node(data)
        pv=self.head 
        NN.next=pv
        self.head=NN
        if self.tail==None:
            self.tail=self.head
        self.size=self.size+1
    def inserte(self,data):
        if self.head==None:
            self.insertb(data)
        else:
            NN=Node(data)
        
            self.tail.next=NN
            self.tail=NN
            self.size=self.size+1
    def insertm(self,data,pos):
        NN=Node(data)
        pv=self.head
        if pos>self.size:
            print("Invalid Position inserting at "+str(pos))
          
            return
        if pos==0:
            self.insertb(data)
        if pos==self.size-1:
            self.inserte(data)
        for i in range(pos):
            if i==pos-1:
                break
           # print(pv.data)
            pv=pv.next
            
        NN.next=pv.next
        pv.next=NN  
        self.size=self.size+1
    def leng(self):
        print("Length of linked list is "+str(self.size))
    def deleb(self):
        
        self.head=self.head.next
        
        if self.head==None:
            self.tail=None
        self.size=self.size-1
    def delee(self):
        pv=self.head
        i=0
        while(i!=self.size-2):
            pv=pv.next
            i=i+1
            
        
        pv.next=None
        self.tail=pv
        self.size=self.size-1
    def delem(self,pos):
        if pos==0:
            self.deleb()
        if pos==self.size-1:
            self.delee()
        pv=self.head
    
        for i in range(pos-1):
            pv=pv.next
            #print(pv.data)
        pv.next=pv.next.next
        self.size=self.size-1
        
        
p=LL()
p.insertb(10)
p.inserte(6)
p.inserte(11)
p.insertb(44)
p.insertm(4, 10)
p.insertm(7,3)
p.insertm(5,0)
p.insertm(8,7)
p.insertm(22,4)
p.deleb()
p.delee()
p.delem(0)
p.delem(1)
p.leng()
p.printf()
            
        
        
        
        
