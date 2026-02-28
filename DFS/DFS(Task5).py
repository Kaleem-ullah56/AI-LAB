import collections
# 1) BFS (Breadth First Search)
def bfs(graph, start):
    visited = set()
    queue = collections.deque([start])
    visited.add(start)
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
# ----------------------------
# 2) DFS (Recursive)
# ----------------------------
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


# 3) DFS using Stack ------------------------------------------------
def dfs_stack(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    stack.append(neighbour)

#-------------------------------------------------------------------
# Inorder, Preorder, Postorder--------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Preorder: We Will move from Root to Left then towards Right
def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)
# Inorder: We Will move from Left to Root then towards Right
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)
# Postorder: We will move from Left to Right then towards Root
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

# ----------------------------
# Main Code
# ----------------------------
if __name__ == "__main__":

    # Graph for BFS and DFS
    graph = {
        0: [1, 2],
        1: [2, 3],
        2: [3],
        3: []
    }
    print("BFS Traversal:")
    bfs(graph, 0)
    print("\nDFS Recursive:")
    dfs(graph, 0)
    print("\nDFS using Stack:")
    dfs_stack(graph, 0)
    print("\n")
    root = Node('A')
    root.left = Node('B')
    root.right = Node('C')
    root.left.left = Node('D')
    root.left.right = Node('E')

    print("Preorder Traversal:")
    preorder(root)

    print("\nInorder Traversal:")
    inorder(root)

    print("\nPostorder Traversal:")
    postorder(root)