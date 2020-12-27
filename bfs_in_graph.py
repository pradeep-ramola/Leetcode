#bfs in graph traversal

from collections import deque
from collections import defaultdict
def bfs(start,visited,path,graph):
    queue= deque()
    path.append(start)
    queue.append(start)
    visited[start]= True
  
    while len(queue)!= 0:
        temp = queue.popleft()
        for neigh in graph[temp]:
            if visited[neigh] == False:
                path.append(neigh)
                queue.append(neigh)
                visited[neigh]=True
        
                
        
        
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
traversedpath=bfs(start,visited,path,graph)
print(traversedpath)

 
