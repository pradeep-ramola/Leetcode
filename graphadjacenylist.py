#undirected graph adjaceny list
'''
V is for vertices and E is for edges


for every edge there is a connection between two nodes/ vetices
let us consider them as
U  V
so i have a graph in which there are 7 vertices(u) and 9 edges(v)
i.e u->v
Now the connection(ab is equal to ba ) 
V E
7 9 first i/p
u V second i/p
A B 
A C
A F
C E
C F
C D
D E
D G
G F
1 2
1 3
1 6
3 5
3 6
3 4
4 5
4 7
7 6
v,e = map(int,input("v and e \n").split())
'''

from collections import defaultdict

graph=defaultdict(list)
# why int becuase we are going to iterate it
v=int(input("Enter no of vertices: \n"))
e=int(input("Enter no of edges : \n"))
print("No of Edges are ",e)
print("No of vertices are ",v)
print("Enter your graph edges one by one like A B or enter evrything once  :\n")
# you can enter your input as A B as A B is one of the edge of your graph your o/p will be same 
#or you can enter your complete input once for eg 
'''
A B 
A C
A F
C E
C F
C D
D E
D G
G F
'''
for i in range(e):
    u,v=map(str,input().split())
    print("your ",i+1,"input is :",u,v)
    graph[u].append(v)
    graph[v].append(u)


for v in graph:
    
    print(v,graph[v])

'''
print(" both function will give same output: \n ")
for u in graph:
    
    print(u,graph[u])
'''
     
