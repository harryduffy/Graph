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

    def dfs(self, begin_id: str, end_id: str):
        
        visited = []
        stack = []
 
        self.dfs_inner(visited, begin_id, end_id, stack)

    def dfs_inner(self, visited, begin_id, end_id, stack):

        stack.append(begin_id)
        visited.append(begin_id)
        if (begin_id.get_id() == end_id.get_id()):
    
            for i in stack:
                print(i.get_id())

            return
        
        for j in begin_id.get_edges():
            
            if (j not in visited):
                self.dfs_inner(visited, j, end_id, stack)
                    
        del stack[-1]

# testing
g = Graph()

# create vertices
A = g.add_vertex('A')
B = g.add_vertex('B')
C = g.add_vertex('C')
D = g.add_vertex('D')
E = g.add_vertex('E')

# create edges
g.add_edge(A, B)
g.add_edge(B, D)
g.add_edge(A, C)
g.add_edge(C, E)
g.add_edge(B, E)

"""
A - B - D
|   |
C - E
"""

g.dfs(D, E)
