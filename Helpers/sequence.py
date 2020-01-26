def to_hash(code_table, dna):
    hash = 0

    for x in dna:
        hash = (hash * 4) + code_table[x]

    return hash

def iterate_hash(hasher, sequence, length, func):
    window = sequence[0:length]
    hash = hasher(window)
    func(0, hash)

    i = length
    window = [hasher(x) for x in window]
    total_bits = 2 ** (2 * length)

    for n in sequence[length:]:
        x = hasher(n)
        index_in_window = (i % length)

        y = window[index_in_window]
        hash = (hash * 4) + x - (y * total_bits)

        func(i - length + 1, hash)
        window[index_in_window] = x
        i += 1