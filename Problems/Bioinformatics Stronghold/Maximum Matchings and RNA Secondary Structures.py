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

    a, u, c, g = nucleotides['A'], nucleotides['U'], nucleotides['C'], nucleotides['G']

    difAU = abs(a - u)
    difCG = abs(c - g)

    possibleAU = factorial(max(a, u)) // factorial(difAU)
    possibleCG = factorial(max(c, g)) // factorial(difCG)

    append(str(int(possibleAU * possibleCG)))

runner.run(run)