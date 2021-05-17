import networkx as nx


def global_clustering_coefficient(g):
    number_of_closed_triplets = 0
    number_of_any_triplets = 0
    num_of_nodes = len(g.nodes)

    # computing number_of_any_triplets
    for i in range(num_of_nodes):
        num_of_neighbors = len(list(g.neighbors(i)))
        number_of_any_triplets += num_of_neighbors * (num_of_neighbors - 1)

    # computing number_of_closed_triplets
    for i in range(num_of_nodes):
        for j in g.neighbors(i):
            for k in g.neighbors(j):
                if i % 5 == 0 and k == 3011:
                    print(i)
                if k != i and g.has_edge(i, k):
                    number_of_closed_triplets += 1
    return number_of_closed_triplets / number_of_any_triplets


def average_clustering_coefficient(g):
    return nx.algorithms.cluster.average_clustering(g)


def local_clustering_coefficients_dict(g):
    return nx.algorithms.cluster.clustering(g)
