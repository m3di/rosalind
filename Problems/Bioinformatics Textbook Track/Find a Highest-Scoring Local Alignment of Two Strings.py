from Problems import runner


def run(input, tokens, append):
    a = tokens[0]
    b = tokens[1]

    sigma = 5
    blosum62 = {}
    temp = """A  C  D  E  F  G  H  I  K  L  M  N  P  Q  R  S  T  V  W  Y
A  2 -2  0  0 -3  1 -1 -1 -1 -2 -1  0  1  0 -2  1  1  0 -6 -3
C -2 12 -5 -5 -4 -3 -3 -2 -5 -6 -5 -4 -3 -5 -4  0 -2 -2 -8  0
D  0 -5  4  3 -6  1  1 -2  0 -4 -3  2 -1  2 -1  0  0 -2 -7 -4
E  0 -5  3  4 -5  0  1 -2  0 -3 -2  1 -1  2 -1  0  0 -2 -7 -4
F -3 -4 -6 -5  9 -5 -2  1 -5  2  0 -3 -5 -5 -4 -3 -3 -1  0  7
G  1 -3  1  0 -5  5 -2 -3 -2 -4 -3  0  0 -1 -3  1  0 -1 -7 -5
H -1 -3  1  1 -2 -2  6 -2  0 -2 -2  2  0  3  2 -1 -1 -2 -3  0
I -1 -2 -2 -2  1 -3 -2  5 -2  2  2 -2 -2 -2 -2 -1  0  4 -5 -1
K -1 -5  0  0 -5 -2  0 -2  5 -3  0  1 -1  1  3  0  0 -2 -3 -4
L -2 -6 -4 -3  2 -4 -2  2 -3  6  4 -3 -3 -2 -3 -3 -2  2 -2 -1
M -1 -5 -3 -2  0 -3 -2  2  0  4  6 -2 -2 -1  0 -2 -1  2 -4 -2
N  0 -4  2  1 -3  0  2 -2  1 -3 -2  2  0  1  0  1  0 -2 -4 -2
P  1 -3 -1 -1 -5  0  0 -2 -1 -3 -2  0  6  0  0  1  0 -1 -6 -5
Q  0 -5  2  2 -5 -1  3 -2  1 -2 -1  1  0  4  1 -1 -1 -2 -5 -4
R -2 -4 -1 -1 -4 -3  2 -2  3 -3  0  0  0  1  6  0 -1 -2  2 -4
S  1  0  0  0 -3  1 -1 -1  0 -3 -2  1  1 -1  0  2  1 -1 -2 -3
T  1 -2  0  0 -3  0 -1  0  0 -2 -1  0  0 -1 -1  1  3  0 -5 -3
V  0 -2 -2 -2 -1 -1 -2  4 -2  2  2 -2 -1 -2 -2 -1  0  4 -6 -2
W -6 -8 -7 -7  0 -7 -3 -5 -3 -2 -4 -4 -6 -5  2 -2 -5 -6 17  0
Y -3  0 -4 -4  7 -5  0 -1 -4 -1 -2 -2 -5 -4 -4 -3 -3 -2  0 10"""

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
        _max = max([0, _d + _s, _i, _j])

        if _max == 0 and 0 not in [_d + _s, _i, _j]:
            return 0, 's'

        if _max == _i:
            return _i, 't'

        if _max == _j:
            return _j, 'l'

        return _max, 'd'

    max_w, max_i, max_j = None, None, None

    while i < ib and j < jb:

        for index in range(j, jb):
            s = compute_score(i, index)
            matrix[i][index] = s

            if max_w is None or max_w < s[0]:
                max_w, max_i, max_j = s[0], i, index

        for index in range(i + 1, ib):
            s = compute_score(index, j)
            matrix[index][j] = s

            if max_w is None or max_w < s[0]:
                max_w, max_i, max_j = s[0], i, index

        i += 1
        j += 1

    _i = max_i - 1
    _j = max_j - 1
    append(str(max_w))

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

        if matrix[_i][_j][1] == 's':
            _i = 0
            _j = 0

    append("\n" + "".join(reversed(aa)))
    append("\n" + "".join(reversed(bb)))


if __name__ == "__main__":
    runner.run(run)
