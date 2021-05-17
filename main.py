import networkx as nx
import InputAndProjection
import ComponentsAnalysis
import ClusterAnalysis


G = InputAndProjection.input_and_project_whole_graph()
# print(ComponentsAnalysis.sizes_of_components(G))

# print(G[2][1]["weight"])

# isolated_tags = []
# ls = ComponentsAnalysis.sizes_of_components(G, 2)
# for i in range(len(ls)):
#     if ls[i] != 0:
#         isolated_tags.append(i + 1)
# print(isolated_tags)

# print(ClusterAnalysis.global_clustering_coefficient(G))
# print(ClusterAnalysis.average_clustering_coefficient(G))
