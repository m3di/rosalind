from Problems import runner


def run(input, tokens, append):
    def neighbours_joining(n, d, nodes=None):
        if nodes is None:
            nodes = list(range(n))

        if n == 2:
            return {
                nodes[0]: {nodes[1]: d[0][1]},
                nodes[1]: {nodes[0]: d[0][1]}
            }

        total_distances = [sum(x) for x in d]

        d_star = [[
            0 if i == j
            else
            (((n - 2) * cell) - total_distances[i] - total_distances[j])
            for j, cell in enumerate(row)
        ] for i, row in enumerate(d)]

        print("d_star is")
        [print(x) for x in d_star]

        # find i and j
        min_w, min_i, min_j = None, 0, 0

        for i in range(n):
            for j in range(i):
                w = d_star[i][j]
                if j != i and (min_w is None or w < min_w):
                    min_w, min_i, min_j = w, i, j

        print("min i,j is", min_i, min_j, "=", min_w, "(" + str(d[min_i][min_j]) + ")")

        delta = (total_distances[min_i] - total_distances[min_j]) / (n - 2)
        print("delta is (%f - %f) / %d" % (total_distances[min_i], total_distances[min_j], n - 2))
        print("delta is", delta)

        ll_i = (d[min_i][min_j] + delta) / 2
        ll_j = (d[min_i][min_j] - delta) / 2

        print("ll i", ll_i)
        print("ll j", ll_j)

        # add parent node
        distance_vector = [(d[k][min_i] + d[k][min_j] - d[min_i][min_j]) / 2 for k in range(n)]

        print("distance vector", distance_vector)

        [d[i].append(distance_vector[i]) for i in range(n)]
        d.append(distance_vector + [0])

        # remove i and j

        d = [[
            cell
            for j, cell in enumerate(row)
            if j not in [min_i, min_j]
        ] for i, row in enumerate(d) if i not in [min_i, min_j]]

        print("updated distance matrix")
        [print(x) for x in d]

        print("nodes before", nodes)

        # generate a new node
        new_node = nodes[-1] + 1
        print("new node", new_node)
        nodes.append(new_node)

        # remove i and j from node list
        label_i, label_j = nodes[min_i], nodes[min_j]
        nodes = [node for index, node in enumerate(nodes) if index not in [min_i, min_j]]

        print("nodes after", nodes)

        tree = neighbours_joining(n - 1, d, nodes)

        if new_node not in tree: tree[new_node] = {}
        if label_i not in tree: tree[label_i] = {}
        if label_j not in tree: tree[label_j] = {}

        tree[label_i][new_node] = ll_i
        tree[new_node][label_i] = ll_i

        tree[label_j][new_node] = ll_j
        tree[new_node][label_j] = ll_j

        return tree

    size = int(tokens[0])
    distance_matrix = []

    for i in range(size):
        index = i * size + 1
        distance_matrix.append([int(x) for x in tokens[index:index + size]])

    tree = neighbours_joining(size, distance_matrix)

    for i in sorted(tree.keys()):
        for j in sorted(tree[i].keys()):
            append("%d->%d:%.3f\n" % (i, j, tree[i][j]))


if __name__ == "__main__":
    runner.run(run)
