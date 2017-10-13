import numpy as np
import solution


class LGIS(solution.Solution):

    @classmethod
    def _read(cls, f):
        _ = next(f)
        return [int(i) for i in next(f).strip().split()]

    @classmethod
    def _solve_helper(cls, data):
        n = len(data)
        data_s = sorted(data)

        # LCS(data, data_s) => LIS
        lcs = np.zeros(n ** 2, dtype=np.int64).reshape((n, n))
        lcs[0][0] = data[0] == data_s[0]

        for i in range(1, n):
            lcs[0][i] = 1 if data[0] == data_s[i] else lcs[0][i - 1]
            lcs[i][0] = 1 if data[i] == data_s[0] else lcs[i - 1][0]

        for i in range(1, n):  # (rows) data
            if i % 100 == 0:
                print(i)

            for j in range(1, n):  # (columns) data_s
                prev_max = max(lcs[i - 1][j - 1], lcs[i, j - 1], lcs[i - 1, j])
                if data[i] == data_s[j]:
                    lcs[i][j] = max(prev_max, lcs[i - 1][j - 1] + 1)
                else:
                    lcs[i][j] = prev_max

        print(lcs)

        i, j = n - 1, n - 1
        res = []

        while i > 0 and j > 0:
            if data[i] == data_s[j]:
                res.append(data[i])
                i -= 1
                j -= 1
            elif lcs[i - 1][j - 1] >= lcs[i - 1][j] and lcs[i - 1][j - 1] >= lcs[i][j - 1]:
                i -= 1
                j -= 1
            elif lcs[i - 1][j] >= lcs[i][j - 1]:
                i -= 1
            else:
                j -= 1

        print()
        return list(reversed(res))

    @classmethod
    def _solve(cls, data):
        a1 = cls._solve_helper(data)
        a2 = [-j for j in cls._solve_helper([-i for i in data])]
        return a1, a2

    @classmethod
    def _write(cls, f, answer):
        for a in answer:
            f.write('{}\n'.format(' '.join([str(i) for i in a])))
