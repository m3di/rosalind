from math import factorial

from Problems import runner


def run(input, tokens, append):
    rna = "".join(tokens[1:])

    complement = {
        'C': 'G',
        'U': 'A',
        'G': 'C',
        'A': 'U',
    }

    def match(a, b):
        return a == complement[b]

    cache = {}

    def partition(seq):
        if len(seq) <= 1:
            return 1

        if seq in cache:
            return cache[seq]

        acc = partition(seq[1:])

        for i in range(1, len(seq)):
            if match(seq[0], seq[i]):
                acc += partition(seq[1:i]) * partition(seq[i + 1:])

        cache[seq] = acc

        return acc

    append(str(partition(rna) % 1000000))


runner.run(run)
