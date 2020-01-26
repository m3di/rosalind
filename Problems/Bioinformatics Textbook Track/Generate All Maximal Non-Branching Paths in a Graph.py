from Problems import runner
from collections import defaultdict


def extract_cycle_starting_at(root_node):
    cycle = [root_node]
    current_node = root_node
    complete = False
    while not complete:
        next_node = graph[current_node][0]
        graph[current_node].remove(next_node)
        if len(graph[current_node]) < 1:
            del graph[current_node]
        cycle.append(next_node)
        current_node = next_node
        complete = (current_node == root_node)
    return cycle


graph = defaultdict(lambda: [])
degrees = defaultdict(lambda: {'in': 0, 'out': 0})


def run(input, tokens, append):
    for i in range(len(tokens) // 3):
        src = tokens[3 * i]
        dests = tokens[3 * i + 2]

        for dest in dests.split(','):
            graph[src].append(dest)

            degrees[src]['out'] += 1
            degrees[dest]['in'] += 1

    paths = []
    visited = {}

    for v in graph:
        if not (degrees[v]['in'] == 1 and degrees[v]['out'] == 1):
            if degrees[v]['out'] > 0:
                for w in graph[v]:
                    path = [v, w]

                    visited[v] = 1
                    visited[w] = 1

                    while degrees[w]['in'] == 1 and degrees[w]['out'] == 1:
                        w = graph[w][0]
                        visited[w] = 1
                        path.append(w)

                    paths.append(path)

    for x in degrees.keys() - visited.keys():
        if x in graph:
            paths.append(extract_cycle_starting_at(x))

    [append(" -> ".join(x) + "\n") for x in paths]


if __name__ == "__main__":
    runner.run(run)
