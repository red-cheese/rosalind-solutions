import numpy as np
import solution
import utils


class CAT(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)[0]

    def solve(self, dna):
        n = len(dna)
        assert n % 2 == 0

        m = np.zeros(n * n, dtype=np.int64).reshape((n, n))

        # Starting values.
        for i in range(n):
            for j in range(n):
                if i == j:
                    m[i][j] = 1

        # Solve for all substrings of length l.
        for l in range(2, n + 2, 2):
            print('l = ', l)

            for i in range(n - l + 1):
                j = i + l - 1
                # Could be smarter when choosing a substring and only include
                # the ones that have the same amount of A/U and C/G. For
                # everything else m[i][j] should be 0 right away.
                subs = dna[i:(j + 1)]  # Include j!!!
                print('i = ', i, 'j = ', j)

                # Possible edges ends on this step.
                ends = [i + 1 + idx for idx, nb in enumerate(subs[1:])
                        if idx % 2 == 0 and nb == utils.RNA_COMPLEMENTS[subs[0]]]
                print('ends: ', ends)

                for end in ends:
                    if end == j:
                        m[i][j] += 1 if i + 1 > j - 1 else m[i + 1][j - 1]

                    elif i + 1 == end:
                        m[i][j] += 1 if i + 2 > j else m[i + 2][j]

                    else:
                        m[i][j] += m[i + 1][end - 1] * m[end + 1][j]

                    m[i][j] %= 1000000

                print('i = ', i, 'j = ', j, 'm =', m[i][j])
            print()

        return m[0][-1]
