import networkx as nx
import InputAndProjection


G = InputAndProjection.input_and_project_graph()
print(G[1][2]["weight"])

