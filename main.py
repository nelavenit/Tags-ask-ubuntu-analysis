import networkx as nx
import InputAndProjection
import ComponentsAnalysis
import ClusterAnalysis as Cluster


G = InputAndProjection.input_and_project_whole_graph()
# print(ComponentsAnalysis.sizes_of_components(G))

# print(G[2][1]["weight"])

# isolated_tags = []
# ls = ComponentsAnalysis.sizes_of_components(G, 2)
# for i in range(len(ls)):
#     if ls[i] != 0:
#         isolated_tags.append(i + 1)
# print(isolated_tags)

# print(Cluster.global_clustering_coefficient(G))
# print(Cluster.average_clustering_coefficient(G))
# print(Cluster.local_clustering_coefficients_dict(G))

# print(Cluster.local_clustering_coefficients_dict(nx.complete_graph(5)))
# print(Cluster.global_clustering_coefficient(nx.complete_graph(5)))
