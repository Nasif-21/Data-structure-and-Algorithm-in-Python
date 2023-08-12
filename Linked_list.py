'''
Lets talk about linked list
In here, a data is stored in the basis of memory location, not based on 
serial. Mainly, we have to implement a data along with its memory locations.
Lets get it straight. 
'''

class Node:
    def __init__(self,key):
        self.key=key
        self.next=None

class Linklist:
    def __init__(self):
        self.head=None


lnklist=Linklist()
lnklist.head= Node('2')
sec= Node('3')
thr= Node('4')

lnklist.head.next=sec
sec.next=thr

while lnklist.head is not None:
    print(lnklist.head.key, end=" ")
    lnklist.head=lnklist.head.next
        
