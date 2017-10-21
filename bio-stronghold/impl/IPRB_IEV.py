import numpy as np
import solution
import utils


class IPRB(solution.SimpleWriteSolution):

    def _read(self, f):
        line = utils.first_line(f)
        return line.split()

    def solve(self, data):
        AA, Aa, aa = data
        AA = float(AA)
        Aa = float(Aa)
        aa = float(aa)
        total = AA + Aa + aa

        aa_aa = aa / total * (aa - 1) / (total - 1)
        Aa_aa = 2 * Aa * aa / total / (total - 1) * 0.5
        Aa_Aa = Aa / total * (Aa - 1) / (total - 1) * 0.25

        return 1 - aa_aa - Aa_aa - Aa_Aa


class IEV(solution.SimpleWriteSolution):

    # AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
    _DOMINANT_WEIGHTS = np.asarray([1., 1., 1., .75, .5, 0.])

    def _read(self, f):
        data = [int(i) for i in utils.first_line(f).split()]
        assert len(data) == 6
        return data

    def solve(self, data):
        return np.dot(self._DOMINANT_WEIGHTS, 2 * np.asarray(data))
