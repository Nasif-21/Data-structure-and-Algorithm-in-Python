'''Lets do the queue implementation in the OOP concept
Very simple
Define functions to work
Apply methods
Call the function with correct parameters
Done


'''

def queue_call():    #For declaring a list
    mylist=[]
    return mylist

def add_item(key,item):     #For pusing elements inside list
    return key.append(item)

def remove_item(key):        #Removng first element from the list
    return key.pop(0)

def check_empty(key):        #Checking the length of the list
    if len(key)==0:
     print ("Empty queue")
    else:
     print ("Current length is = ",len(key))


    

    



arr=queue_call()
print(str(arr))
add_item(arr,4)
add_item(arr,3)
add_item(arr,7)
add_item(arr,9)
print("Element inside list is "+ str(arr))
check_empty(arr)
remove_item(arr)
print("Element inside list is "+ str(arr))
check_empty(arr)
remove_item(arr)
print("Element inside list is "+ str(arr))
check_empty(arr)
remove_item(arr)
print("Element inside list is "+ str(arr))
check_empty(arr)
remove_item(arr)
print("Element inside list is "+ str(arr))
check_empty(arr)
