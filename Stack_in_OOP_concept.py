'''
Stack in OOP concept may look quite hard. But let me help you out
First define a function for stack
Declare another function to define the stack if empty
Function for push an element into it
Function for pop of stack
'''
def create():            #Creating an function
    element=[]     
    return element

def check_len(element):   #Length of the element
     if len(element)==0:
          print("Empty stack")
     else:
          print("The size of stack is =" ,len(element))
         

def element_push(element,item):  #Pushing an element
     return element.append(item)
 
def element_pop(element):        #Removing an element
     return element.pop()
    
        

   


arr=create()           #Now, defined worl
print(arr)             
check_len(arr)
element_push(arr,2)
element_push(arr,6)
element_push(arr,9)
element_push(arr,5)
print(arr)
check_len(arr)
element_pop(arr)                                  #Poping the elements
print(arr)
check_len(arr)



