#BFS QUEUED
graph = { 
'A':['B', 'C'],
 'B':['D', 'E'],
 'C': ['F'],
 'D': ['G','H'],
 'E': [],
 'F':['I','K'],
 'G':[],
 'H':['L'],
 'I':[],
 'K':['M'],
 'L':[],
 'M':[]
}
# BFS WITH QUEUE
from collections import deque

def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print(node)

        if node not in visited:
            visited.append(node)

            for child in graph[node]:
                queue.append(child)
# Already Provided
def dls(start,goal,path,lavel,max):
 print(lavel)
 print(start)
 path.append(start)
 if start==goal:
  return path
 if lavel==max:
  return path
 for child in graph[start]:
  if dls(child,goal,path,lavel+1,max):
   return path
 path.pop()
 return False
start='A'
goal=input("enter the goal state")
max=int(input("enter the limit"))
path=list()
# Priniting oF code
print("BFS With Queue:")
bfs(start)

print("DLS Result:")
res=dls(start,goal,path,0,max)

if res:
 print(path)