from graph import Graph


if __name__ == '__main__':
    # vertices_with_neighbours = {1: [2, 3], 2: [4], 3: [4, 5], 4: [], 5: []}
    vertices_with_neighbours = {1: [2], 2: [], 3: [4], 4: []}
    x = Graph(vertices_with_neighbours)
    print(x.get_neighbours())
    print(x.get_vertices())
    x.add({5: []})
    print(x.get_neighbours())
    print(x.get_vertices())
