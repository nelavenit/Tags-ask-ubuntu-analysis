# BFS
def sizes_of_components(g):  # returns list of components sizes
    component_number = -1
    used = []
    component = []
    num = len(list(g.nodes))
    for i in range(num):
        used.append(False)

    for i in range(num):
        if not used[i]:
            component_number += 1
            queue = [i]
            component.append(0)
            while queue:
                j = queue.pop()
                used[j] = True
                component[component_number] += 1
                neighbors = list(g.neighbors(j))
                for to in range(len(neighbors)):
                    if not used[neighbors[to]]:
                        queue.append(neighbors[to])
    return component
