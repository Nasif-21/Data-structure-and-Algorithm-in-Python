'''
Lets understand the concept of stack
Stack is a data static data structure where LIFO application'
is applied.Its like a storage where we pick out the last entried
data. To do so, we need to do Push and Pop
First, make a stack
Then append some data
When we pop the data, it will take out the last index from its
dataset.
Its liner data structure and its complexity is O(1)
Lets work it on basic structure and then to the oop structure

'''

stack=[]                #Creating an empty stack

stack.append(1)         #Add elements
stack.append(5)
stack.append(3)
stack.append(9)

print("Element inside stacks right now is"+str(stack)) #Datas inside the stack
print("Poping an item")
stack.pop()                                            #Poping a data, you will see the last element is being remove
print("Element inside stacks right now is"+str(stack)) #Check output