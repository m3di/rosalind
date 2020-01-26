from math import factorial

from Problems import runner


def run(input, tokens, append):
    k = int(tokens[0])
    dna = tokens[1]
    l = len(dna)

    graph = {}
    last = False

    for i in range(0, l - k + 2):
        kmer = dna[i:i + k - 1]

        if last != False:

            if last not in graph:
                graph[last] = []

            graph[last].append(kmer)

        last = kmer

    [append("%s -> %s\n" % (key, ",".join(val))) for key, val in graph.items()]


if __name__ == "__main__":
    runner.run(run)
