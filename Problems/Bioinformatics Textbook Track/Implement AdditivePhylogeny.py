from Problems import runner

new_node_counter = 0


def ll(distance_matrix, node):
    return min([
        (distance_matrix[i][node] + distance_matrix[node][j] - distance_matrix[i][j]) // 2
        for i in range(len(distance_matrix)) for j in range(len(distance_matrix))
        if i != node and j != node and i != j
    ])


def run(input, tokens, append):
    global new_node_counter

    def find_leaves(node, D):
        for i in range(len(D)):
            for j in range(len(D)):
                if D[i][j] == D[i][node] + D[node][j] and i != j:
                    return i, node, j

    def travers(adjacency_list, start, end, path=None, weights=None):
        if path is None:
            path = [start]

        if weights is None:
            weights = [0]

        for j, w in adjacency_list[start].items():
            if j in path:
                continue

            new_path = path + [j]
            new_weights = weights + [w]

            p, w = travers(adjacency_list, j, end, new_path, new_weights)

            if p[-1] == end:
                return p, w

        return path, weights

    def attachment_position(path, weights, x):
        total = 0
        prev_node = None

        for l, w in zip(path, weights):
            along_here = total
            total += w
            if total == x:
                return True, l, l, along_here, total
            if total > x:
                return False, prev_node, l, along_here, total
            prev_node = l

        print("whaaat???")

    def additive_phylogeny(N, D):
        global new_node_counter

        if N == 2:
            print("generating tree ...")
            return {
                0: {1: D[0][1]},
                1: {0: D[0][1]}
            }

        print("solving for", N, D)

        # always select the last node
        node = N - 1
        print("selected node is", node)

        limb_length = ll(D, node)
        print("limb length is", limb_length)

        for i in range(node):
            D[node][i] -= limb_length
            D[i][node] = D[node][i]

        print("reduced matrix is", D)

        i, n, k = find_leaves(node, D)
        print("selected leaves are", i, n, k)

        x = D[i][n]
        print("x is", x)

        print("generating tree for ", N - 1, "------------")
        T = additive_phylogeny(N - 1, [z[:-1] for z in D[:-1]])
        print("--------------")
        print("result is", T)

        print("ok let's find the path between %s and %s" % (i, k))
        path, weights = travers(T, i, k)
        print("selected path is", path)

        exists, a, b, before, after = attachment_position(path, weights, x)

        if node not in T:
            T[node] = {}

        if exists:
            T[node][a] = limb_length
            T[a][node] = limb_length
        else:
            print("we must add a node between %s and %s" % (a, b))
            print("new node is", new_node_counter)
            print("before is ", T)
            # remove the existing node
            T[a].pop(b)
            T[b].pop(a)
            # add a new node
            T[new_node_counter] = {}

            T[a][new_node_counter] = x - before
            T[new_node_counter][a] = x - before

            T[b][new_node_counter] = after - x
            T[new_node_counter][b] = after - x

            T[node][new_node_counter] = limb_length
            T[new_node_counter][node] = limb_length
            print("after is ", T)

            new_node_counter += 1

        return T

    size = int(tokens[0])
    distance_matrix = []

    for i in range(size):
        index = i * size + 1
        distance_matrix.append([int(x) for x in tokens[i * size + 1:index + size]])

    new_node_counter = size
    tree = additive_phylogeny(size, distance_matrix)
    [[append("%d->%d:%d\n" % (n1, n2, w)) for n2, w in x.items()] for n1, x in tree.items()]


if __name__ == "__main__":
    runner.run(run)
