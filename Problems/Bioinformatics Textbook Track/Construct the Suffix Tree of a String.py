from Problems import runner


def compress(root, label=''):
    if type(root) is not dict:
        return root, label

    if len(root.keys()) == 1:
        key, val = list(root.items())[0]
        return compress(val, label + key)

    vs = {}

    for i, vertices in root.items():
        sub_tree, sub_label = compress(vertices, i)
        vs[sub_label] = sub_tree

    return vs, label


def run(input, tokens, append):
    text = tokens[0]

    suffix_trie = {}

    for i in range(len(text)):
        parent = None
        current = suffix_trie

        for j in text[i:]:
            if j not in current:
                current[j] = {}
            parent = current
            current = current[j]

        parent = i

    suffix_trie, label = compress(suffix_trie)

    queue = [suffix_trie]
    parts = []

    while (len(queue) > 0):
        current = queue.pop()

        for key, val in current.items():
            if len(key) > 0:
                parts.append(key)

            if type(val) is dict:
                queue.append(val)

    append("\n".join(parts))


if __name__ == "__main__":
    runner.run(run)
