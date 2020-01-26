from Problems import runner


def run(input, tokens, append):
    a = tokens[0]
    b = tokens[1]

    sigma = 5
    blosum62 = {}
    temp = """A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7"""

    rows = temp.splitlines()
    first_row = [x.strip() for x in rows[0].split(' ') if len(x.strip()) > 0]
    for row in rows[1:]:
        cols = [x.strip() for x in row.split(' ') if len(x.strip()) > 0]
        row_label = cols[0]
        if row_label not in blosum62:
            blosum62[row_label] = {}
        for w, col_label in zip(cols[1:], first_row):
            blosum62[row_label][col_label] = int(w)

    matrix = [[0 for x in range(len(b) + 1)] for x in range(len(a) + 1)]

    i, ib, j, jb = 0, len(a) + 1, 0, len(b) + 1

    def compute_score(ii, jj):
        if ii == 0 and jj == 0:
            return 0, 'd'

        if ii == 0:
            return matrix[i][jj - 1][0] - sigma, 'l'

        if jj == 0:
            return matrix[ii - 1][j][0] - sigma, 't'

        _i = matrix[ii - 1][jj][0] - sigma
        _j = matrix[ii][jj - 1][0] - sigma
        _d = matrix[ii - 1][jj - 1][0]
        _s = blosum62[a[ii - 1]][b[jj - 1]]
        _max = max([_d + _s, _i, _j])

        if _max == _i:
            return _i, 't'

        if _max == _j:
            return _j, 'l'

        return _max, 'd'

    while i < ib and j < jb:

        for index in range(j, jb):
            matrix[i][index] = compute_score(i, index)

        for index in range(i + 1, ib):
            matrix[index][j] = compute_score(index, j)

        i += 1
        j += 1

    _i = ib - 1
    _j = jb - 1
    append(str(matrix[_i][_j][0]))

    aa = []
    bb = []

    while _i > 0 or _j > 0:
        if matrix[_i][_j][1] == 'd':
            aa.append(a[_i - 1])
            bb.append(b[_j - 1])
            _i -= 1
            _j -= 1

        if matrix[_i][_j][1] == 'l':
            aa.append('-')
            bb.append(b[_j - 1])
            _j -= 1

        if matrix[_i][_j][1] == 't':
            aa.append(a[_i - 1])
            bb.append('-')
            _i -= 1

    append("\n" + "".join(reversed(aa)))
    append("\n" + "".join(reversed(bb)))


if __name__ == "__main__":
    runner.run(run)
