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

    states = [
        {
            'A': log(1 / 2 * emissions['A'][string[0]]),
            'B': log(1 / 2 * emissions['B'][string[0]])
        }
    ]

    states_s = []

    for ob in string[1:]:
        last_state = states[-1]
        present_state = {}
        present_state_s = {}

        for ps in last_state:
            __max, __max_s = float('-inf'), None

            for ls in last_state:
                c = last_state[ls] * transition[ls][ps]

                if __max < c:
                    __max, __max_s = c, ls

            present_state[ps] = __max * emissions[ps][ob]
            present_state_s[ps] = __max_s

        states.append(present_state)
        states_s.append(present_state_s)

    path = []

    path.append(max(states[-1].items(), key=operator.itemgetter(1))[0])
    for i in range(len(states_s) - 1, -1, -1):
        path.append(states_s[i][path[-1]])
    append("".join(reversed(path)))


if __name__ == "__main__":
    runner.run(run)
