from Problems import runner

graph = {}


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


def extract_eulerian_circuit(root):
    cycle = extract_cycle_starting_at(root)
    print("main cycle extracted: " + "->".join(cycle))

    while len(graph) > 0:
        for index, node in enumerate(cycle):
            if node in graph:
                new_cycle = extract_cycle_starting_at(node)
                print("found new cycle to merge: " + "->".join(new_cycle))
                cycle = cycle[:index] + new_cycle + cycle[index + 1:]
                break

    return cycle


def run(input, tokens, append):
    degrees = {}

    for i in range(len(tokens) // 3):
        src = tokens[3 * i]
        dests = tokens[3 * i + 2]

        graph[src] = []
        if src not in degrees: degrees[src] = {'out': 0, 'in': 0}

        for dest in dests.split(','):
            if dest not in degrees: degrees[dest] = {'out': 0, 'in': 0}
            graph[src].append(dest)
            degrees[src]['out'] += 1
            degrees[dest]['in'] += 1

    begin = [x for x in degrees if degrees[x]['out'] - degrees[x]['in'] == 1]
    end = [x for x in degrees if degrees[x]['in'] - degrees[x]['out'] == 1]

    print("begin detected: " + begin[0])
    print("end detected: " + end[0])

    if end[0] not in graph: graph[end[0]] = []
    graph[end[0]].append(begin[0])

    path = extract_eulerian_circuit(begin[0])
    append("->".join(path[:-1]))


if __name__ == "__main__":
    runner.run(run)
