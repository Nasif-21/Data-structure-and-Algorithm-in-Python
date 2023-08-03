''' We are going to understand the basic of search method.
in this case, we are going to use an array with 5 elements 
where we will look for specific number.
If the number is in the array, it will return its index number,
if not, it will send -1 insted


Logic for code: First define an function. If you think its not worthy or difficult for 
you, just skip ok!
So, after you declare an array, just make a search till its length. 
Now you wanna search that number, just match with its element at all the index.
When it will find out the number, the code stops to generate and return you its index
number.

Lets go for it!!!!!

'''



def lnSearch(elements, key):               #Defining a function
    for i in range(len(elements)):         #Searching an element till its length
        if elements[i]==key:               #Find out the key , if matches
         return i                          #Return its index number
    return -1
suspects=[1,3,6,9,8,7,4]
print (lnSearch(suspects,9))
print ("If non elemental like 5, we will get:")
print(lnSearch(suspects,5))

    
