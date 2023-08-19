'''
Lets talk about graph theory. Graph is nothing but connection between various nodes with
edges. For work purpose, we will be given a graph to deploy. The edged are connected to each other 
need to be connected with each other. 
Lets do one basic code to understand it

'''

graph= {
    'A': ['B','E'],
    'B':['A','C','D'],
    'C':['B','D'],
    'D':['B','C','E'],
    'E':['A','B','D'],

}                     
for key,val in graph.items():
    print(f"{key}-->{val}")   