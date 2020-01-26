def run(problem):
    inputFile = open("../../input.txt", "r")
    rawContent = inputFile.read()
    inputFile.close()

    tokens = []

    for line in rawContent.splitlines():
        for t in line.split():
            if len(t) > 0:
                tokens.append(t)

    output = []

    def appendToOutput(string):
        output.append(string)

    problem(rawContent, tokens, appendToOutput)
    output = "".join(output)

    print(output)

    out = open("../../output.txt", "w")
    out.write(output)
    out.close()
