import numpy as np
import solution
import utils
from impl import HAMM


class PDST(solution.Solution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)

    def solve(self, data):
        m = np.zeros(shape=(len(data), len(data)))

        for i in range(0, len(data)):
            for j in range(i + 1, len(data)):
                assert len(data[i]) == len(data[j])
                m[i][j] = m[j][i] = HAMM.HAMM().solve((data[i], data[j])) / len(data[i])

        return m

    def _write(self, f, m):
        for row in m:
            f.write(' '.join(str(d) for d in row) + '\n')
