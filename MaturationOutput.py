import config as cfg
import InputAndProjection
import ComponentsAnalysis
import ClusterAnalysis


def number_of_components_maturation():
    ls = []
    for i in range(2, cfg.maximum_edge_degree + 1):
        g = InputAndProjection.input_and_project_graph(i)
        ls.append(len(ComponentsAnalysis.sizes_of_components(g)))
    return ls


def largest_component_size_maturation():
    ls = []
    for max_deg in range(2, cfg.maximum_edge_degree + 1):
        g = InputAndProjection.input_and_project_graph(max_deg)
        sizes = ComponentsAnalysis.sizes_of_components(g)
        ls.append(max(sizes) / cfg.total_number_of_nodes)
    return ls


# value_metric is either arithmetic mean or geometric mean
def global_clustering_coefficient_maturation(weighted=False, value_metric="arithmetic mean"):
    ls = []
    for max_deg in range(2, cfg.maximum_edge_degree + 1):
        g = InputAndProjection.input_and_project_graph(max_deg)
        if not weighted:
            ls.append(ClusterAnalysis.global_clustering_coefficient(g))
        else:
            ls.append(ClusterAnalysis.global_clustering_coefficient_for_weighted_projection(g, value_metric))
    return ls


def average_clustering_coefficient_maturation():
    ls = []
    for max_deg in range(2, cfg.maximum_edge_degree + 1):
        g = InputAndProjection.input_and_project_graph(max_deg)
        ls.append(ClusterAnalysis.average_clustering_coefficient(g))
    return ls
