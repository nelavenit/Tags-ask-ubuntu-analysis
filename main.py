import networkx as nx
import ClusterAnalysis
import MaturationOutput
import InputAndProjection
import ComponentsAnalysis
import ClusterAnalysis as Cluster
import matplotlib as mpl
import matplotlib.pyplot as plt

file = open("output.txt", "w")
ls = MaturationOutput.global_clustering_coefficient_maturation(True, "arithmetic mean")
for element in ls:
    file.write(str(element) + '\n')
