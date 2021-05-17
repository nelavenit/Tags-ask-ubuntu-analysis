import networkx as nx
import InputAndProjection
import ComponentsAnalysis


G = InputAndProjection.input_and_project_whole_graph()
# print(ComponentsAnalysis.sizes_of_components(G))

# print(G[2][1]["weight"])

# ls = ComponentsAnalysis.sizes_of_components(G, 2)
# for i in range(len(ls)):
#     if ls[i] != 0:
#         print(i + 1)
