import matplotlib.pyplot as plt
import config as cfg
import InputAndProjection
import ComponentsAnalysis
import ClusterAnalysis


def number_of_components_maturation():
    ls = []
    for i in range(2, cfg.maximum_edge_degree + 1):
        g = InputAndProjection.input_and_project_graph(i)
        ls.append(len(ComponentsAnalysis.sizes_of_components(g)))

    plt.plot(range(2, cfg.maximum_edge_degree + 1), ls, 'o--r')
    plt.xlabel("Maximum edge degree")
    plt.ylabel("Number of components")
    plt.title("Number of components maturation")
    plt.show()


def largest_component_size_maturation():
    ls = []
    for max_deg in range(2, cfg.maximum_edge_degree + 1):
        g = InputAndProjection.input_and_project_graph(max_deg)
        sizes = ComponentsAnalysis.sizes_of_components(g)
        ls.append(max(sizes) / cfg.total_number_of_nodes)
    plt.plot(range(2, cfg.maximum_edge_degree + 1), ls, 'o--r')
    plt.xlabel("Maximum edge degree")
    plt.ylabel("Relative size of the largest component")
    plt.title("Relative size of the largest component maturation")
    plt.show()


# Either "auto-scale"  or "from zero to one" for the interval of [0, 1]
# value_metric is either arithmetic mean or geometric mean
def global_clustering_coefficient_maturation(mode="auto-scale", weighted=False, value_metric="arithmetic mean"):
    ls = []
    for max_deg in range(2, cfg.maximum_edge_degree + 1):
        g = InputAndProjection.input_and_project_graph(max_deg)
        if not weighted:
            ls.append(ClusterAnalysis.global_clustering_coefficient(g))
        else:
            ls.append(ClusterAnalysis.global_clustering_coefficient_for_weighted_projection(g, value_metric))

    plt.plot(range(2, cfg.maximum_edge_degree + 1), ls, 'o--r')
    if mode == "from zero to one":
        plt.axis([2 - cfg.graphics_margins, cfg.maximum_edge_degree + cfg.graphics_margins,
                  -cfg.graphics_margins, 1 + cfg.graphics_margins])
    plt.xlabel("Maximum edge degree")
    plt.ylabel("Global clustering coefficient")
    plt.title("Global clustering coefficient maturation")
    plt.show()


# Either "auto-scale"  or "from zero to one" for the interval of [0, 1]
def average_clustering_coefficient_maturation(mode="auto-scale"):
    ls = []
    for max_deg in range(2, cfg.maximum_edge_degree + 1):
        g = InputAndProjection.input_and_project_graph(max_deg)
        ls.append(ClusterAnalysis.average_clustering_coefficient(g))
    plt.plot(range(2, cfg.maximum_edge_degree + 1), ls, 'o--r')
    if mode == "from zero to one":
        plt.axis([2 - cfg.graphics_margins, cfg.maximum_edge_degree + cfg.graphics_margins,
                  -cfg.graphics_margins, 1 + cfg.graphics_margins])
    plt.xlabel("Maximum edge degree")
    plt.ylabel("Average clustering coefficient")
    plt.title("Average clustering coefficient maturation")
    plt.show()
