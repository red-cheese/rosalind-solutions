import numpy as np
import solution
import utils


class EDIT(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)

    def solve(self, data):
        """Levenshtein distance."""

        prot1, prot2 = data
        lev = np.zeros(shape=(len(prot1), len(prot2)), dtype=np.int64)
        lev[0][0] = 0 if prot1[0] == prot2[0] else 1

        for i in range(1, len(prot1)):
            lev[i][0] = lev[i - 1][0] + i
        for j in range(1, len(prot2)):
            lev[0][j] = lev[0][j - 1] + j

        for i in range(1, len(prot1)):
            for j in range(1, len(prot2)):
                lev[i][j] = min(
                    lev[i - 1][j - 1] + (0 if prot1[i] == prot2[j] else 1),
                    lev[i - 1][j] + 1,
                    lev[i][j - 1] + 1
                )

        return lev[-1][-1]
