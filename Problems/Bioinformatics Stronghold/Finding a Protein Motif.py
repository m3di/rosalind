from Problems import runner
import urllib.request


def run(input, tokens, append):
    for protein in tokens:
        if len(protein) > 0:
            print("fetching " + protein)

            url = "http://www.uniprot.org/uniprot/%s.fasta" % protein

            fasta = []
            buffer = ""

            content = urllib.request.urlopen(url).read()
            print("> fasta loaded [" + str(content) + "]")

            for line in content.decode('utf-8').splitlines():
                if line[0] == '>':
                    if len(buffer) > 0:
                        fasta.append(buffer)
                    buffer = ""
                else:
                    buffer += line

            if len(buffer) > 0:
                fasta.append(buffer)

            sequence = fasta[0]
            positions = []

            for i in range(0, len(sequence) - 4 + 1):
                if (sequence[i] == 'N') and (sequence[i + 1] != 'P') and (sequence[i + 2] in ['S', 'T']) and (
                        sequence[i + 3] != 'P'):
                    positions.append(str(i + 1))

            if len(positions) > 0:
                append(protein)
                append("\n")
                append(" ".join(positions))
                append("\n")
            else:
                print("no position founded")


runner.run(run)
