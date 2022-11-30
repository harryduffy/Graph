from Vertex import Vertex

class Graph:

    def __init__(self):
        self._vertices = []
        self._size = 0

    def add_vertex(self, vertex):

        new_vertex = Vertex(vertex)
        self._vertices.append(new_vertex)
        self._size += 1

        return new_vertex

    def add_edge(self, v1, v2):

        if v1.set_edge(v2) and ((v1 and v2) in self.get_vertices()):
            return 1

        return 0

    def get_vertices(self):
        return self._vertices

    def dfs_util(self, v, visited):
 
        # Mark the current node as visited
        visited.append(v)
        print(v.get_id())
 
        # recurse through the vertices adjacent to this vertex
        for adj in v.get_edges():

            # only visit unvisited vertices
            if adj not in visited:
                self.dfs_util(adj, visited)

    def DFS(self, v):
 
        visited = []
 
        self.dfs_util(v, visited)

# testing
g = Graph()

# create vertices
A = g.add_vertex('A')
B = g.add_vertex('B')
C = g.add_vertex('C')
D = g.add_vertex('D')

# create edges
g.add_edge(A, B)
g.add_edge(B, D)
g.add_edge(A, C)

"""
A - B - D
|
C
"""

g.DFS(B)




