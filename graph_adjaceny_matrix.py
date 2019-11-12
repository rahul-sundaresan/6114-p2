infinity = 9999


class GraphAdjacencyMatrix:
    def __init__(self, vertices_count):
        self.vertices_count = vertices_count
        self.adjacency_matrix = [[infinity] * vertices_count for _ in range(vertices_count)]

    def print_adjacency_matrix(self):
        for i in range(self.vertices_count):
            for j in range(self.vertices_count):
                print(self.adjacency_matrix[i][j], ",", end="")
            print("")

    def set_distance(self, row, column,distance):
        self.adjacency_matrix[row][column] = distance


if __name__ == '__main__':
    g= GraphAdjacencyMatrix(3)
    g.print_adjacency_matrix()