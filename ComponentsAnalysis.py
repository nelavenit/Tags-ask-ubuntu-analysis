# BFS
# 1 - returns list of components sizes, 2 - returns list showing which component node belongs to
def sizes_of_components(g, mode=1):
    component_number = -1
    used = []
    components_sizes = []
    component_marks = []
    num = len(list(g.nodes))
    for i in range(num):
        used.append(False)
        component_marks.append(0)

    for i in range(num):
        if not used[i]:
            component_number += 1
            queue = [i]
            components_sizes.append(0)
            while queue:
                j = queue.pop()
                if used[j]:
                    continue
                used[j] = True
                components_sizes[component_number] += 1
                component_marks[j] = component_number
                neighbors = list(g.neighbors(j))
                for to in range(len(neighbors)):
                    if not used[neighbors[to]]:
                        queue.append(neighbors[to])
    if mode == 1:
        return components_sizes
    elif mode == 2:
        return component_marks
