'''
Lets alk about queue. Its a  data structure where an item came to the last and 
goes out first. For example, in a line, you guys are waiting for the food in KFC.
The person standing at the first will be served first. In this manner, the first
guy came got the first order. 
In the world of data structure, queue is same to the KFC line. 
To do so, lets follow an simple steps
First, Declare an empty list {which works like an array in other programming language}
Then append some items.
In this stack, kick out the first elements from the list
done
Lets implement!!!
'''

queue_list=[]            #Defining a queue list

queue_list.append(5)     #Appending an item
queue_list.append(3)
queue_list.append(8)
queue_list.append(9)

print("Items in queue " +str(queue_list))

queue_list.pop(0)   #Removing the first index 

print("Items in queue " +str(queue_list))

queue_list.pop(0)
print("Items in queue " +str(queue_list))




