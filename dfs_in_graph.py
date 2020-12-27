#dfs traversal of undirected graph
#you can use this code for directed graph as well with small changes such as  make changes in the append of u and v
#u will be appended to v if there is a directed arrow from u->v not bot sides as we are doing here you can add code like graph[v].append(u) or opposite 
from collections import defaultdict
def dfs(start,visited,path,graph):
    path.append(start)
    visited[start]= True
    for neighbournode in graph[start]:
        #print(graph[start])
        if visited[neighbournode] == False:
            #print("this is current graph neighbour :",neighbournode) 
            dfs(neighbournode,visited,path,graph)
    return path


#using dictionary as key value pair (value which will be list) 
graph=defaultdict(list)

v,e=map(int,input("Enter the no of vetrices and edges present in graph :  ").split())
#entery of graph nodes
for i in range(e):
    u,v=map(str,input("Enter the node/vertex and its neighbour : ").split())
    graph[u].append(v)
    graph[v].append(u)

#print(graph)
#printing adjacency list of graph nodes
print("Your ADJACENY GRAPH LIST  is :  ")
for v in graph:
    print(v,graph[v])

start=input("Enter your starting node : ")
#print(graph[start])
# to keep track of visited nodes 
visited=defaultdict(bool)
path=[]
traversedpath=dfs(start,visited,path,graph)
print(traversedpath)
    
