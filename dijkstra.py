import graph_adjaceny_matrix as graph
import  parse_text_to_graph
infinity = 9999


def find_minimum_distance(passed_graph, distance_list, cloud):
    minimum_distance = infinity
    for vertex in range(passed_graph.vertices_count):
        if distance_list[vertex] < minimum_distance and vertex not in cloud:
            minimum_distance = distance_list[vertex]
            return vertex


def find_shortest_path(passed_graph, source_node, vertex_list):
    # initialize distances to all nodes to infinity
    distance_list = [infinity] * passed_graph.vertices_count
    distance_list[source_node] = 0
    cloud = []
    for i in range(passed_graph.vertices_count):
        minimum_node = find_minimum_distance(passed_graph, distance_list, cloud)
        cloud.append(minimum_node)
        for vertex in range(passed_graph.vertices_count):
            if passed_graph.adjacency_matrix[minimum_node][vertex] > 0 and vertex not in cloud and \
                   distance_list[vertex] > distance_list[minimum_node] + passed_graph.adjacency_matrix[minimum_node][vertex]:
                distance_list[vertex] = distance_list[minimum_node] + passed_graph.adjacency_matrix[minimum_node][vertex]
    display_shortest_paths(distance_list, passed_graph, vertex_list)


def display_shortest_paths(distance_list, passed_graph, vertex_list):
    for vertex_index in range(passed_graph.vertices_count):
        print("vertex ", vertex_list[vertex_index],  " is at distance ", distance_list[vertex_index])


if __name__ == '__main__':
    file = input("name of file:")
    given_graph, vertex_list, start_vertex = parse_text_to_graph.read_file(file)
    find_shortest_path(given_graph, vertex_list.index(start_vertex), vertex_list)
