class EdgeRepresentation:
    def __init__(self,u,v,edge_length):
        self.u = u
        self.v = v
        self.edge_length = edge_length

    def __lt__(self, other):
        return self.edge_length < other.edge_length

    def __str__(self):
        return self.u + "<-----" + str(self.edge_length) + "----->" + self.v

def edge_already_in_list(edge: EdgeRepresentation, given_list):
    e1 = False
    e2 = False
    for included_edge in given_list:
        if edge.u == included_edge.u or edge.u == included_edge.v:
            e1 = True
        else:
            return False
    for included_edge in given_list:
        if edge.v == included_edge.u or edge.v == included_edge.v:
            e2 = True
    if e1 and e2
        return True
    return False


def kruskal_mst(sorted_edges):
    max_edges = len(sorted_edges)
    current_edges = []
    current_edge_count = 0
    current_edges = [sorted_edges[0:2]] # safely add first 2 edges because they can't form loops
    current_edge_count += 2
    for edge in sorted_edges:
        while current_edge_count < max_edges:
            if edge_already_in_list(edge,current_edges):
                pass
            else:
                current_edges.append(edge)
                current_edge_count += 1
    return current_edges




if __name__ == '__main__':
    e = EdgeRepresentation('a', 'b', 6)
    k = EdgeRepresentation('b', 'e', 4)
    le = [e, k]
    eek = le.sort()
    for edge in le:
        print(edge)
