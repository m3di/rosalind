from Problems import runner


def run(input, tokens, append):
    str = tokens[0]

    prob = {
        'A': {
            'A': float(tokens[8]),
            'B': float(tokens[9]),
        },
        'B': {
            'A': float(tokens[11]),
            'B': float(tokens[12]),
        }
    }

    total = 1/2

    for a,b in zip(str[:-1], str[1:]):
        total *= prob[a][b]

    print(total)


if __name__ == "__main__":
    runner.run(run)
