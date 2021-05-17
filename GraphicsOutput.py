import matplotlib as mpl
import matplotlib.pyplot as plt
import config
import InputAndProjection
import ComponentsAnalysis
import ClusterAnalysis


def number_of_components_maturation():
    ls = []
    for i in range(1, config.maximum_edge_degree + 1):
        g = InputAndProjection.input_and_project_graph(i)
        ls.append(len(ComponentsAnalysis.sizes_of_components(g)))
    plt.plot(range(config.maximum_edge_degree), ls, 'o--r')
    plt.xlabel("Maximum edge degree")
    plt.ylabel("Number of components")
    plt.title("Number of components maturation")
    plt.show()


def largest_component_size_maturation():
    ls = []
    for max_deg in range(1, config.maximum_edge_degree + 1):
        g = InputAndProjection.input_and_project_graph(max_deg)
        sizes = ComponentsAnalysis.sizes_of_components(g)
        ls.append(min(sizes) / config.total_number_of_nodes)

    plt.plot(range(config.maximum_edge_degree), ls, 'o--r')
    plt.xlabel("Maximum edge degree")
    plt.ylabel("Relative size of largest component")
    plt.title("Size of largest maturation")
    plt.show()

