from Helpers.DNA import DNA_CODON_TABLE
from Problems import runner


def run(input, tokens, append):
    fasta = []
    buffer = ""

    for nucleotide in tokens:
        if nucleotide[0] == '>':
            if len(buffer) > 0:
                fasta.append(buffer)
            buffer = ""
        else:
            buffer += nucleotide

    if len(buffer) > 0:
        fasta.append(buffer)

    introns = fasta[1:]
    dna = fasta[0]

    lengths = [len(x) for x in introns]
    counters = lengths[:]

    i = 0
    l = len(dna)

    while i < l:
        nucleotide = dna[i]

        for intron_index, intron in enumerate(introns):

            if nucleotide == intron[lengths[intron_index] - counters[intron_index]]:
                counters[intron_index] -= 1
            else:
                while counters[intron_index] < lengths[intron_index]:
                    counters[intron_index] += 1

                    if nucleotide == intron[lengths[intron_index] - counters[intron_index]]:
                        counters[intron_index] -= 1
                        break

            if (counters[intron_index]) == 0:
                dna = dna[0: i - lengths[intron_index] + 1:] + dna[i + 1::]

                i -= lengths[intron_index]
                l -= lengths[intron_index]
                counters = lengths[:]

                break

        i += 1

    for i in range(0, len(dna), 3):
        codon = dna[i:i + 3]

        try:
            protein = DNA_CODON_TABLE[codon]

            if protein == "-":
                break

            append(DNA_CODON_TABLE[codon])
        except KeyError:
            pass


runner.run(run)
