import random

class Graph:
    def __init__(self, vertices_with_neighbours):
        self.vertices_with_neighbours = vertices_with_neighbours
        self.vertices = self.get_all_vertices()
        self.repair_neighbour()
        self.I = self.find_mis()

    def get_all_vertices(self):
        return set(self.vertices_with_neighbours.keys())

    def get_neighbours(self):
        return self.vertices_with_neighbours

    def repair_neighbour(self):
        for v1 in self.vertices:
            for v2 in self.vertices_with_neighbours[v1]:
                if v1 not in self.vertices_with_neighbours[v2]:
                    self.vertices_with_neighbours[v2].append(v1)

    def get_vertices(self):
        return self.I

    def find_mis(self):
        set_I = set()
        vertices_cp = self.vertices.copy()
        while vertices_cp:
            n = len(vertices_cp)
            v = list(vertices_cp)[random.randint(0, n-1)]
            set_I |= {v}
            vertices_cp -= {v}
            vertices_cp -= set(self.vertices_with_neighbours[v])
        return set_I

    def add(self, v):
        self.vertices |= v.keys()
        self.vertices_with_neighbours.update(v)
        self.repair_neighbour()
        for v_no in v.keys():
            if not set(v[v_no]) & self.I:
                self.I |= {v_no}
