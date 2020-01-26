from Problems import runner
from collections import defaultdict


def run(input, tokens, append):
    last_column = list(tokens[0])
    first_column = "".join(list(sorted(last_column)))

    for find in tokens[1:]:
        top = 0
        bottom = len(last_column) - 1

        while top <= bottom:
            if len(find) > 0:
                symbol = find[-1]
                find = find[:-1]
                if symbol in last_column[top:bottom + 1]:
                    top = first_column.find(symbol) + last_column[0:top].count(symbol)
                    bottom = first_column.find(symbol) + last_column[0:bottom + 1].count(symbol) - 1
                else:
                    append(str(0))
                    break
            else:
                append(str(bottom - top + 1))
                break

        append(" ")


if __name__ == "__main__":
    runner.run(run)
