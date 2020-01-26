from Problems import runner
from random import sample


def get_score(graph, g_lables, leafs, labels):
    node_count = len(graph)
    score = {}

    def score_of(v):
        r = []

        for s in list('ACGT'):
            nn = []

            for node in graph[v]:
                nn.append(min(score[node][i] + (0 if s == ss else 1) for i, ss in enumerate(list('ACGT'))))

            r.append(sum(nn))

        return r

    for node in leafs:
        score[node] = [0 if c == labels[node] else float('inf') for c in list('ACGT')]

    while node_count > len(score):
        for v, edges in graph.items():
            if v not in score and False not in [e in score for e in edges]:
                score[v] = score_of(v)
                break

    root = list(score.keys())[-1]
    if root not in g_lables: g_lables[root] = ''
    g_lables[root] += list('ACGT')[score[root].index(min(score[root]))]

    def track(o_node, label):
        for node in graph[o_node]:
            if node not in leafs and node != o_node:
                if node not in g_lables: g_lables[node] = ''
                min_score = min([score[node][i] for i in range(4)])
                idx = [i for i in range(4) if score[node][i] == min_score]
                flag = True

                for i in idx:
                    if list('ACGT')[i] == label:
                        flag = False
                        g_lables[node] += label
                        track(node, label)

                if flag:
                    g_lables[node] += list('ACGT')[sample(idx, 1)[0]]
                    track(node, g_lables[node][-1])

    track(root, g_lables[root][-1])
    return min([score[root][x] for x in range(4)])


def run(input, tokens, append):
    graph = {}

    labels = {}
    leafs = []
    assigned_labels = {}

    n = int(tokens[0])

    def format_node(node):

        if str.isdigit(node):
            return int(node)

        if node in assigned_labels:
            return assigned_labels[node]

        lbl = len(labels)
        labels[lbl] = node
        leafs.append(lbl)

        assigned_labels[node] = lbl

        return lbl

    for edge in tokens[1:]:
        begin, end = edge.split('->')
        begin, end = format_node(begin), format_node(end)
        if begin not in graph: graph[begin] = []
        graph[begin].append(end)

    pivot_1 = max(list(graph.keys()))
    pivot_2 = max(graph[pivot_1])
    new_node = pivot_1 + 1
    graph[pivot_1].remove(pivot_2)
    graph[pivot_2].remove(pivot_1)
    graph[new_node] = [pivot_2, pivot_1]

    def to_directed(root):
        for x in graph[root]:
            if root in graph[x]:
                graph[x].remove(root)
            to_directed(x)

    to_directed(new_node)

    scores = []
    char_length = len(list(labels.values())[0])
    g_labels = labels.copy()

    for i in range(char_length):
        lbls = {}

        for node, label in labels.items():
            lbls[node] = label[i]

        scores.append(get_score(graph, g_labels, leafs, lbls))

    append(str(sum(scores)) + "\n")

    del graph[new_node]
    graph[pivot_1].append(pivot_2)
    graph[pivot_2].append(pivot_1)

    printed = []

    for node in sorted(list(graph.keys()) + leafs):
        if node in graph:
            for next in graph[node]:
                if node in g_labels and next in g_labels and (node, next) not in printed:
                    l1, l2 = g_labels[node], g_labels[next]
                    hamming = sum([1 if a != b else 0 for a, b in zip(l1, l2)])
                    append("%s->%s:%d\n" % (l1, l2, hamming))
                    append("%s->%s:%d\n" % (l2, l1, hamming))
                    printed.append((node, next))
                    printed.append((next, node))


if __name__ == "__main__":
    runner.run(run)
