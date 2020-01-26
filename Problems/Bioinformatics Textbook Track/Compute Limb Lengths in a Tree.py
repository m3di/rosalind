from Problems import runner


def ll(distance_matrix, node):
    return min([
        (distance_matrix[i][node] + distance_matrix[node][j] - distance_matrix[i][j]) // 2
        for i in range(len(distance_matrix)) for j in range(len(distance_matrix))
        if i != node and j != node and i != j
    ])


def run(input, tokens, append):
    n = int(tokens[0])
    j = int(tokens[1])
    distance_matrix = []

    for i in range(n):
        index = i * n + 2
        distance_matrix.append([int(x) for x in tokens[index:index + n]])
    print(n, j, distance_matrix)

    append(str(ll(distance_matrix, j)))


if __name__ == "__main__":
    runner.run(run)
