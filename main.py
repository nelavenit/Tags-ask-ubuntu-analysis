import networkx as nx
import InputAndProjection
import ComponentsAnalysis


G = InputAndProjection.input_and_project_whole_graph()
print(ComponentsAnalysis.sizes_of_components(G))
# print(G[2][1]["weight"])
