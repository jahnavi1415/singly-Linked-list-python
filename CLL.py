# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 12:01:28 2023

@author: janib
"""

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertb(self,data):
        NN=Node(data)
        if self.head==None:
            self.head=NN
            self.tail=NN
            return
       
        NN.next=self.head
            
        self.tail.next=NN
        self.tail=NN
    def printf(self):
        pv=self.head
        if(self.head!=None):
            print(pv.data)
            pv=pv.next
        while(pv!=self.head):
            print(pv.data)
            pv=pv.next
    def dele(self,data):
        pv=self.head
        if pv==None:
            print("G")
            return
        if pv.data==data:
            self.head=self.head.next 
            self.tail.next=self.head
            return
        if pv.next.data==data:
            pv.next=pv.next.next
            return
        pv=pv.next
        while(pv!=self.head):
            if pv.next.data==data:
                pv.next=pv.next.next
            pv=pv.next
        
            
            
        
F=CLL()
F.insertb(4)
F.insertb(8)
F.insertb(5)
F.insertb(9)
F.insertb(2)
F.dele(8)
F.dele(4)
F.dele(2)
F.printf()

        
