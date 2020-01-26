from Problems import runner
from itertools import product
from math import inf


def hamming(a, b):
    return sum([1 if i != j else 0 for i, j in zip(a, b)])


def run(input, tokens, append):
    k = int(tokens[0])
    collection = tokens[1:]

    best = None
    best_score = inf

    for pattern in product('ACGT', repeat=k):
        score = 0

        for dna in collection:
            score += min([hamming(pattern, dna[i:i + k]) for i in range(0, len(dna) - k + 1)])

        if score < best_score:
            best, best_score = pattern, score

    append("".join(best))


if __name__ == "__main__":
    runner.run(run)
