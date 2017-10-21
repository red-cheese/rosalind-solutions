import numpy as np
import solution
import utils


class CAT(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)[0]

    def solve(self, dna):
        n = len(dna)
        assert n % 2 == 0

        # Starting values.
        m = np.eye(n, dtype=int)

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


class MOTZ(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)[0]

    def solve(self, rna):
        """Similarly to "Catalan" numbers above - solve for all substrings of
        len l for l in range(n)."""

        n = len(rna)
        # Answers for substrings from i to j.
        motz = np.eye(n, dtype=int)

        for l in range(2, n + 1):
            print('l = ', l)

            for i in range(n - l + 1):
                j = i + l - 1
                assert i < j
                # print('i = ', i, 'j = ', j)

                # If rna[i] doesn't have an edge.
                motz[i][j] += motz[i + 1][j]

                # If rna[i] has an edge - possible edges ends on this step.
                ends = [k for k in range(i + 1, j + 1)
                        if rna[k] == utils.RNA_COMPLEMENTS[rna[i]]]
                # print('ends: ', ends)

                for end in ends:
                    if end == j:
                        motz[i][j] += 1 if i + 1 > j - 1 else motz[i + 1][j - 1]

                    elif i + 1 == end:
                        motz[i][j] += 1 if i + 2 > j else motz[i + 2][j]

                    else:
                        motz[i][j] += motz[i + 1][end - 1] * motz[end + 1][j]

                    motz[i][j] %= 1000000

                # print('i = ', i, 'j = ', j, 'm =', motz[i][j])

            print()

        return motz[0][-1]
