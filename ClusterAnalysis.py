import networkx as nx
import math


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
                if k != i and g.has_edge(i, k):
                    number_of_closed_triplets += 1
    return number_of_closed_triplets / number_of_any_triplets


# Either arithmetic or geometric mean to count triplet value
def global_clustering_coefficient_for_weighted_projection(g, mode="arithmetic mean"):
    total_closed_triplets_value = 0
    total_triplets_value = 0
    num_of_nodes = len(g.nodes)

    # computing both total_triplets_value and total_closed_triplets_value
    for i in range(num_of_nodes):
        num_of_neighbors = len(g.neighbors(i))
        for j in range(num_of_neighbors):
            for k in range(j + 1, num_of_neighbors):
                u = g.neighbors(i)[j]
                v = g.neighbors(i)[k]
                num_of_edges = 2
                if g.has_edge(u, v):
                    num_of_edges = 3

                # arithmetic mean
                if mode == "arithmetic mean":
                    if num_of_edges == 2:
                        # I don't divide by 2 because we multiply by 2 to consider all the triplets
                        total_triplets_value += g[i][u]["weight"] + g[i][v]["weight"]
                    if num_of_edges == 3:
                        value = (g[i][v]["weight"] + g[i][u]["weight"] + g[u][v]["weight"]) / 3
                        total_triplets_value += value
                        total_closed_triplets_value += value
                # geometric mean
                if mode == "geometric mean":
                    if num_of_edges == 2:
                        total_triplets_value += 2 * math.sqrt(g[i][u]["weight"] * g[i][v]["weight"])
                    if num_of_edges == 3:
                        value = (g[i][u]["weight"] * g[i][v]["weight"] * g[u][v]["weight"]) ** 1/3
                        total_triplets_value += value
                        total_closed_triplets_value += value

    return total_closed_triplets_value / total_triplets_value


def average_clustering_coefficient(g):
    return nx.algorithms.cluster.average_clustering(g)


def local_clustering_coefficients_list(g):
    return list(nx.algorithms.cluster.clustering(g).values())
