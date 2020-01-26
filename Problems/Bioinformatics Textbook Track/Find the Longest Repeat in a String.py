from Problems import runner


def discover(root, deep=0):
    pass


def run(input, tokens, append):
    text = tokens[0] + "$"

    suffix_trie = {}

    for i in range(len(text)):
        parent = None
        current = suffix_trie

        for j in text[i:]:
            if j not in current:
                current[j] = {}
            parent = current
            current = current[j]

        parent['$'] = i

    queue = [suffix_trie]
    parts = []

    while (len(queue) > 0):
        current = queue.pop()

        for key, val in current.items():
            if type(val) is dict:
                queue.append(val)

    print(suffix_trie)
    # append("\n".join(parts))


if __name__ == "__main__":
    runner.run(run)
