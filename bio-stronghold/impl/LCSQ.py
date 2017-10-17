import numpy as np
import solution
import utils


class LCSQ(solution.Solution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)

    def _solve(self, data):
        s1, s2 = data
        n = len(s1)
        m = len(s2)

        lcs = np.zeros(n * m, dtype=np.int64).reshape((n, m))
        lcs[0][0] = s1[0] == s2[0]

        for i in range(1, n):
            lcs[i][0] = 1 if s1[i] == s2[0] else lcs[i - 1][0]
        for j in range(1, m):
            lcs[0][j] = 1 if s1[0] == s2[j] else lcs[0][j - 1]

        for i in range(1, n):
            for j in range(1, m):
                lcs[i][j] = lcs[i - 1][j - 1] + 1 if s1[i] == s2[j] else max(lcs[i, j - 1], lcs[i - 1, j])

        i, j = n - 1, m - 1
        res = []

        while i >= 0 and j >= 0:
            if s1[i] == s2[j]:
                res.append(s1[i])
                i -= 1
                j -= 1
            elif (i > 0 and lcs[i - 1][j] >= lcs[i][j - 1]) or j == 0:
                i -= 1
            else:
                assert j > 0
                j -= 1

        return list(reversed(res))

    def _write(self, f, answer):
        f.write(''.join(answer))
