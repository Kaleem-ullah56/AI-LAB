from collections import deque
# OOP was used in this programme 
class Graph:
    # Constructor (init)
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    # to Get neighbors of a node
    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # It's a Heuristic function
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1
        }
        return H[n]

    # A* Algorithm
    def a_star_algorithm(self, start_node, stop_node):

        open_list = set([start_node])
        closed_list = set([])

        g = {}
        g[start_node] = 0

        parents = {}
        parents[start_node] = start_node

        while open_list:

            n = None

            # Find node with lowest using a formula f(n) = g(n) + h(n)
            for v in open_list:
                if n is None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v

            if n is None:
                print("Path does not exist!")
                return None

            # incase the goal is reached
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)
                reconst_path.reverse()

                print("Path found:", reconst_path)
                return reconst_path

            # Checking of neighbors
            for (m, weight) in self.get_neighbors(n):

                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                else:
                    if g.get(m, float('inf')) > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            open_list.remove(n)
            closed_list.add(n)

        print("Path does not exist!")
        return None


# data of Graph
adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)],
    'D': []
}
graph1 = Graph(adjacency_list)

# Running of A*
graph1.a_star_algorithm('A', 'D')