#BFS Without Queue
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
# Addition of BFS(Without Queued)
def bfs(start):
    visited = []
    data = [start]

    while data:
        node = data.pop(0)
        print(node)

        if node not in visited:
            visited.append(node)

            for child in graph[node]:
                data.append(child)
#Already Provided 
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

#Printing of Code
print("BFS Without Queue:")
bfs(start)

print("DLS Result:")
res=dls(start,goal,path,0,max)

if res:
 print(path)