from Problems import runner


def run(input, tokens, append):
    size = int(tokens[0])
    distance_matrix = {}

    nodes = [str(x) for x in range(size)]

    for i in nodes:
        index = int(i) * size + 1
        distance_matrix[i] = dict(zip(nodes, [int(x) for x in tokens[index:index + size]]))

    new_node_counter = size
    ages = {}
    tree = {}

    clusters = {}

    while len(distance_matrix) > 1:
        min_w, min_i, min_j = None, 0, 0

        for i, neighbours in distance_matrix.items():
            for j, w in neighbours.items():
                if j != i and (min_w is None or w < min_w):
                    min_w, min_i, min_j = w, i, j

        i_vect = distance_matrix.pop(min_i)
        j_vect = distance_matrix.pop(min_j)
        [(x.pop(min_i), x.pop(min_j)) for node, x in distance_matrix.items()]

        new_node = str(new_node_counter)
        distance_matrix[new_node] = {}
        clusters[new_node] = clusters.get(min_i, [min_i]) + clusters.get(min_j, [min_j])

        for node in distance_matrix:
            if node == new_node:
                distance_matrix[node][node] = 0
            else:
                len_i = len(clusters.get(min_i, [1]))
                len_j = len(clusters.get(min_j, [1]))
                w = (i_vect[node] * len_i + j_vect[node] * len_j) / (len_i + len_j)
                distance_matrix[node][new_node] = w
                distance_matrix[new_node][node] = w

        age = min_w / 2

        age_i = age - ages.get(min_i, 0)
        age_j = age - ages.get(min_j, 0)

        ages[new_node] = age

        tree[new_node] = {min_i: age_i, min_j: age_j}
        tree[min_i] = {**tree.get(min_i, {}), **{new_node: age_i}}
        tree[min_j] = {**tree.get(min_j, {}), **{new_node: age_j}}

        new_node_counter += 1

    [[append("%s->%s:%.3f\n" % (n1, n2, w)) for n2, w in x.items()] for n1, x in tree.items()]


if __name__ == "__main__":
    runner.run(run)
