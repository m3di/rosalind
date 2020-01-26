from Problems import runner


def run(input, tokens, append):
    outcomes = tokens[0]
    states = tokens[6]

    prob = {
        'A': {
            'x': float(tokens[15]),
            'y': float(tokens[16]),
            'z': float(tokens[17]),
        },
        'B': {
            'x': float(tokens[19]),
            'y': float(tokens[20]),
            'z': float(tokens[21]),
        }
    }

    total = 1

    for s, o in zip(states, outcomes):
        total *= prob[s][o]

    append(str(total))


if __name__ == "__main__":
    runner.run(run)
