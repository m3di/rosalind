from Helpers.sequence import to_hash as generic_hash, iterate_hash as generic_iterate_hash

DNA_CODE_TABLE = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3,
}


def to_hash(dna):
    return generic_hash(DNA_CODE_TABLE, dna)


def iterate_hash(dna, window, func):
    return generic_iterate_hash(to_hash, dna, window, func)
