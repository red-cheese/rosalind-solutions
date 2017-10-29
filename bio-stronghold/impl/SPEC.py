import numpy as np
import solution
import utils


class SPEC(solution.SimpleWriteSolution):

    _EPSILON = .0001

    def _read(self, f):
        return [float(i.strip()) for i in list(f)]

    def solve(self, spectrum):
        diff = np.asarray(spectrum[1:]) - np.asarray(spectrum[:-1])
        res = []
        for d in diff:
            for k, v in utils.PROT_MASS_TABLE.items():
                if abs(v - d) < self._EPSILON:
                    res.append(k)
                    break

        assert len(res) == len(spectrum) - 1

        return ''.join(res)
