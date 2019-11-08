import graph_adjaceny_matrix as graph

infinity = float('inf')


def display_shortest_paths(distance_list, passed_graph):
    for vertex in range(passed_graph.vertices_count):
        print("vertex ", vertex,  " is at distance ", distance_list[vertex])


def find_minimum_distance(passed_graph, distance_list, cloud):
    minimum_distance = infinity
    for vertex in range(passed_graph.vertices_count):
        if distance_list[vertex] < minimum_distance and vertex not in cloud:
            minimum_distance = distance_list[vertex]
            return vertex


def find_shortest_path(passed_graph, source_node):
    # initialize distances to all nodes to infinity
    distance_list = [infinity] * passed_graph.vertices_count
    distance_list[source_node] = 0
    cloud = []
    for i in range(passed_graph.vertices_count):
        minimum_node = find_minimum_distance(passed_graph,distance_list, cloud)
        cloud.append(minimum_node)
        for vertex in range(passed_graph.vertices_count):
            if passed_graph.adjacency_matrix[minimum_node][vertex] > 0 and vertex not in cloud and \
              0      distance_list[vertex] > distance_list[minimum_node] + passed_graph.adjacency_matrix[minimum_node][vertex]:
                distance_list[vertex] = distance_list[minimum_node] + passed_graph.adjacency_matrix[minimum_node][vertex]
    display_shortest_paths(distance_list,passed_graph)

if __name__ == '__main__':
    g = graph.GraphAdjacencyMatrix(9)
    g.adjacency_matrix = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                           [4, 0, 8, 0, 0, 0, 0, 11, 0],
                           [0, 8, 0, 7, 0, 4, 0, 0, 2],
                           [0, 0, 7, 0, 9, 14, 0, 0, 0],
                           [0, 0, 0, 9, 0, 10, 0, 0, 0],
                           [0, 0, 4, 14, 10, 0, 2, 0, 0],
                           [0, 0, 0, 0, 0, 2, 0, 1, 6],
                           [8, 11, 0, 0, 0, 0, 1, 0, 7],
                           [0, 0, 2, 0, 0, 0, 6, 7, 0]
                           ]
    find_shortest_path(g, 0)
