import numpy as np
import solution


class HAMM(solution.SimpleWriteSolution):

    def _read(self, f):
        lines = [line.strip() for line in f if line.strip()]
        assert len(lines) == 2
        return lines

    def solve(self, data):
        dna1, dna2 = data

        dna1 = np.asarray(list(dna1))
        dna2 = np.asarray(list(dna2))
        assert len(dna1) == len(dna2)

        return np.sum(dna1 != dna2)
