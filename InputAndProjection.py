import networkx as nx
from config import total_number_of_nodes
from config import weighing_mode


def input_and_project_whole_graph():
    edge_degree_list = open("Dataset/tags-ask-ubuntu-nverts.txt", "r")
    nodes_connected_by_edge = open("Dataset/tags-ask-ubuntu-simplices.txt", "r")

    g = nx.Graph()
    g.add_nodes_from(range(total_number_of_nodes))
    for line in edge_degree_list.readlines():
        num_of_nodes = int(line[:-1:])
        list_of_nodes = []  # List of nodes in edge
        for i in range(num_of_nodes):
            node = int(nodes_connected_by_edge.readline()[:-1:])
            list_of_nodes.append(node)
        for i in range(num_of_nodes):
            for j in range(i + 1, num_of_nodes):
                u = list_of_nodes[i] - 1
                v = list_of_nodes[j] - 1
                if weighing_mode == 1:
                    if g.has_edge(u, v):
                        g[u][v]["weight"] += 1
                    else:
                        g.add_edge(u, v, weight=1)
                elif weighing_mode == 0:
                    if not g.has_edge(u, v):
                        g.add_edge(u, v, weight=1)
                elif weighing_mode == 2:
                    if g.has_edge(u, v):
                        g[u][v]["weight"] += 1/num_of_nodes
                    else:
                        g.add_edge(u, v, weight=1/num_of_nodes)
    return g
