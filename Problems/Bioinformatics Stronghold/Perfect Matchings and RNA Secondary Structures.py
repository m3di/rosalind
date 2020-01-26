from math import factorial

from Problems import runner


def run(input, tokens, append):
    rna = "".join(tokens[1:])

    nucleotides = {}

    for nucleotide in rna:
        try:
            nucleotides[nucleotide] += 1
        except KeyError:
            nucleotides[nucleotide] = 1

    append(str(factorial(nucleotides['A']) * factorial(nucleotides['C'])))


runner.run(run)
