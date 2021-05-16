import networkx as nx

total_number_of_nodes = 3029
weighing_mode = 1  # 0 - unweighted, 1 - weight of node = number of times two tags met together

edge_degree_list = open("Dataset/tags-ask-ubuntu-nverts.txt", "r")
nodes_connected_by_edge = open("Dataset/tags-ask-ubuntu-simplices.txt", "r")

G = nx.Graph(weight=1)
G.add_nodes_from(range(1, total_number_of_nodes + 1))
for line in edge_degree_list.readlines():
    num_of_nodes = int(line[:-1:])
    list_of_nodes = []  # List of nodes in edge
    for i in range(num_of_nodes):
        node = int(nodes_connected_by_edge.readline()[:-1:])
        list_of_nodes.append(node)
    for i in range(num_of_nodes):
        for j in range(i + 1, num_of_nodes):
            u = list_of_nodes[i]
            v = list_of_nodes[j]
            if weighing_mode == 1:
                if G.has_edge(u, v):
                    G[u][v]["weight"] += 1
                else:
                    G.add_edge(u, v, weight=1)
            else:
                if not G.has_edge(u, v):
                    G.add_edge(u, v, weight=1)

