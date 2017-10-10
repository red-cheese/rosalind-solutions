import numpy as np
import solution
import utils


class CONS(solution.Solution):

    _NAME = 'CONS'

    _IDX = ['A', 'C', 'G', 'T']

    @classmethod
    def _read(cls, f):
        dnas = [list(dna) for _, dna in utils.read_fasta(f)]
        return np.asarray(dnas)

    @classmethod
    def _solve(cls, data):
        rows, cols = data.shape

        profile = np.zeros(4 * cols, dtype=np.int32).reshape((4, cols))
        # Should use np.where but too lazy...
        for dna in data:
            for col in range(cols):
                profile[cls._IDX.index(dna[col])][col] += 1

        cons = ''.join([cls._IDX[i] for i in np.argmax(profile, axis=0)])

        return profile, cons

    @classmethod
    def _write(cls, f, answer):
        profile, cons = answer
        f.write(cons)
        f.write('\n')
        for i, row in enumerate(profile):
            f.write('{}: {}'.format(cls._IDX[i], ' '.join(str(j) for j in row)))
            f.write('\n')
