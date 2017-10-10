import numpy as np
import solution


class CONS(solution.Solution):

    _NAME = 'CONS'

    _IDX = ['A', 'C', 'G', 'T']

    @classmethod
    def _read(cls, f):
        dnas = []

        dna = ''

        for line in f:
            line = line.strip()

            if line.startswith('>'):
                # Flush the old dna.
                    if dna:
                        dnas.append(list(dna))
                    dna = ''
            else:
                dna += line

        # Flush the last one.
        dnas.append(list(dna))

        l = len(dnas[0])
        assert all([len(dna) == l for dna in dnas])

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
