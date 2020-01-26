import operator
from Problems import runner


def log(x):
    return x


def run(input, tokens, append):
    string = tokens[0]

    # @todo: consider using dynamic data structure

    transition = {
        'A': {
            'A': log(float(tokens[12])),
            'B': log(float(tokens[13]))
        },
        'B': {
            'A': log(float(tokens[15])),
            'B': log(float(tokens[16]))
        }
    }

    emissions = {
        'A': {
            'x': log(float(tokens[22])),
            'y': log(float(tokens[23])),
            'z': log(float(tokens[24])),
        },
        'B': {
            'x': log(float(tokens[26])),
            'y': log(float(tokens[27])),
            'z': log(float(tokens[28])),
        }
    }

    forward = [
        {
            'A': log(1 / 2 * emissions['A'][string[0]]),
            'B': log(1 / 2 * emissions['B'][string[0]])
        }
    ]

    for ob in string[1:]:
        last_state = forward[-1]
        present_state = {}
        for ps in last_state:
            present_state[ps] = sum([last_state[ls] * transition[ls][ps] for ls in last_state]) * emissions[ps][ob]
        forward.append(present_state)

    backward = [
        {
            'A': log(1 / 2 * emissions['A'][string[-1]]),
            'B': log(1 / 2 * emissions['B'][string[-1]])
        }
    ]

    for ob in list(reversed(string[:-1])):
        last_state = backward[-1]
        present_state = {}
        for ps in last_state:
            present_state[ps] = sum([last_state[ls] * transition[ps][ls] for ls in last_state]) * emissions[ps][ob]
        backward.append(present_state)

    for x, y in zip(forward, reversed(backward)):
        px = sum([a * b for a, b in zip(x.values(), y.values())])
        print("%.4f %.4f" % (x['A'] * y['A'] / px, x['B'] * y['B'] / px))


if __name__ == "__main__":
    runner.run(run)
