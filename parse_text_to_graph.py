import graph_adjaceny_matrix as graph


def read_file(filename):
    with open(filename, 'r') as graph_file:
        vertex_list = []
        is_directed_graph = False
        start_vertex = ""
        # read first line, remove trailing whitespace and split on space
        graph_details = graph_file.readline().rstrip().split(' ')
        vertices_count = int(graph_details[0])

        if graph_details[2] == 'D':
            is_directed_graph = True

        graph_adjacency_matrix = graph.GraphAdjacencyMatrix(vertices_count)
        for line in graph_file:
            data = line.rstrip().split(' ')
            if len(data) == 1:  # if start vertex is specified, use it otherwise it's the first vertex in the txt file
                start_vertex = data[0]
                break
            vertex_1 = data[0]
            vertex_2 = data[1]
            distance = int(data[2])
            if vertex_1 not in vertex_list:
                vertex_list.append(vertex_1)
            if vertex_2 not in vertex_list:
                vertex_list.append(vertex_2)

            start_vertex = vertex_list[0]
            row = vertex_list.index(vertex_1)
            column = vertex_list.index(vertex_2)
            graph_adjacency_matrix.set_distance(row, column, distance)
            if not is_directed_graph:
                graph_adjacency_matrix.set_distance(column, row, distance)
        return graph_adjacency_matrix, vertex_list, start_vertex


if __name__ == '__main__':
    g, d, start_vertex = read_file("sample.txt")
    g.print_adjacency_matrix()
    print("Vertices:", d)
    print("start vertex:", start_vertex)
