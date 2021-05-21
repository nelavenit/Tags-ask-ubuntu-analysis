import matplotlib.pyplot as plt
import config as cfg


# Scale is either "auto scale" or "from 0 to 1"
def maturation_plot(values_list, plot_title, y_axis_label, x_axis_label="Maximum edge degree",
                    scale="auto-scale", margin=cfg.default_plot_margin):
    plt.plot(range(2, cfg.maximum_edge_degree + 1), values_list, 'o--r')
    if scale == "from 0 to 1":
        plt.axis([2 - margin, cfg.maximum_edge_degree + margin,
                  -margin, 1 + margin])
    plt.xlabel(x_axis_label)
    plt.ylabel(y_axis_label)
    plt.title(plot_title)
    plt.show()
