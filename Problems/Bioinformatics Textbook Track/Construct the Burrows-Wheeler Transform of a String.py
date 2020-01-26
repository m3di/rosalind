from Problems import runner


def run(input, tokens, append):
    string = tokens[0]
    doubled = tokens[0] * 2

    rotations = sorted([doubled[i:i + len(string)] for i in range(0, len(string))])
    bwt = "".join([i[-1] for i in rotations])

    append(bwt)


if __name__ == "__main__":
    runner.run(run)
