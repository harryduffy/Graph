class Vertex:

    def __init__(self, id):
        self._id = id
        self._edges = []

    def get_edges(self):
        return self._edges

    def set_edge(self, vertex):

        if vertex:
            self._edges.append(vertex)
            vertex._edges.append(self)
        else:
            return 0

        return 1

    def get_id(self):
        return self._id
