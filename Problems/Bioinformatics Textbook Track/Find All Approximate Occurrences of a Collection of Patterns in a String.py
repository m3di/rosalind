from functools import cmp_to_key
from Problems import runner
from math import ceil

suffix_array = []
bwt_last = []
bwt_first = []
bwt_count = []
bwt_first_index = {}


def build_suffix_array(genome):
    l = len(genome)

    def compare(i, j):
        while i < l and j < l:
            if genome[i] > genome[j]:
                return 1
            elif genome[i] < genome[j]:
                return -1
            i += 1
            j += 1
        return 0

    return sorted(range(len(genome)), key=cmp_to_key(compare))


def build_bwt(genome):
    doubled = genome * 2
    rotations = sorted([doubled[i:i + len(genome)] for i in range(0, len(genome))])
    return [i[-1] for i in rotations]


def bwt_find(pattern):
    top = 0
    bottom = len(bwt_last) - 1
    while top <= bottom:
        if pattern:
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if bwt_count[bottom + 1][symbol] > bwt_count[top][symbol]:
                top = bwt_first_index[symbol] + bwt_count[top][symbol]
                bottom = bwt_first_index[symbol] + bwt_count[bottom + 1][symbol] - 1
            else:
                return []
        else:
            return [suffix_array[i] for i in range(top, bottom + 1)]
    return []


def hamming(s1, s2):
    mismatches = 0
    for key, val in enumerate(s1):
        if val != s2[key]:
            mismatches += 1
    return mismatches


def run(input, tokens, append):
    global suffix_array, bwt_last, bwt_first, bwt_count, bwt_first_index

    genome = tokens[0] + "$"
    patterns = tokens[1:-1]
    d = int(tokens[-1])

    suffix_array = build_suffix_array(genome)
    bwt_last = build_bwt(genome)
    bwt_first = sorted(bwt_last)

    bwt_count = [{'A': 0, 'C': 0, 'G': 0, 'T': 0}]

    for partition in bwt_last:
        bwt_count.append(bwt_count[-1].copy())

        if partition != '$':
            bwt_count[-1][partition] += 1

    bwt_first_index = {}

    for key, val in enumerate(bwt_first):
        if val not in bwt_first_index:
            bwt_first_index[val] = key

    positions = []

    for pattern in patterns:
        occurrences = []
        print("-- %s is the pattern" % pattern)
        l = len(pattern)
        seed_size = ceil(l / (d + 1))
        partitions = [(x, pattern[x:x + seed_size]) for x in range(0, l, seed_size)]
        print("partitions are [%s]" % " ".join(x[1] for x in partitions))

        for partition_offset, partition_str in partitions:
            for partition_position in bwt_find(partition_str):
                print("partition %s occurred in %d" % (partition_str, partition_position))
                total_offset = partition_position - partition_offset
                founded_match = genome[total_offset:total_offset + len(pattern)]
                print("-- %s is a candidate " % founded_match)
                if len(founded_match) == len(pattern):
                    print("they have same size")
                    print("hamming distance is %d" % hamming(pattern, founded_match))
                    if hamming(pattern, founded_match) <= d:
                        print("so we're good, adding %d" % total_offset)
                        if total_offset not in occurrences:
                            occurrences.append(total_offset)
                    else:
                        print("no thanks :)")
                else:
                    print("they are not same size")
        positions.extend(occurrences)

    append(" ".join([str(x) for x in positions]))


if __name__ == "__main__":
    runner.run(run)
