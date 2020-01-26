from Helpers.sequence import to_hash as generic_hash, iterate_hash as generic_iterate_hash

DNA_CODE_TABLE = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3,
}

DNA_CODON_TABLE = {
    'TTT': 'F', 'CTT': 'L', 'ATT': 'I', 'GTT': 'V',
    'TTC': 'F', 'CTC': 'L', 'ATC': 'I', 'GTC': 'V',
    'TTA': 'L', 'CTA': 'L', 'ATA': 'I', 'GTA': 'V',
    'TTG': 'L', 'CTG': 'L', 'ATG': 'M', 'GTG': 'V',
    'TCT': 'S', 'CCT': 'P', 'ACT': 'T', 'GCT': 'A',
    'TCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
    'TCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
    'TCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
    'TAT': 'Y', 'CAT': 'H', 'AAT': 'N', 'GAT': 'D',
    'TAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
    'TAA': '-', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
    'TAG': '-', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
    'TGT': 'C', 'CGT': 'R', 'AGT': 'S', 'GGT': 'G',
    'TGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
    'TGA': '-', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
    'TGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
}


def to_hash(dna):
    return generic_hash(DNA_CODE_TABLE, dna)


def iterate_hash(dna, window, func):
    return generic_iterate_hash(to_hash, dna, window, func)
