import solution
import utils
from scipy.special import binom


class LIA(solution.SimpleWriteSolution):

    @classmethod
    def _read(cls, f):
        k, N = utils.first_line(f).split()
        return int(k), int(N)

    @classmethod
    def _solve(cls, data):
        """See file LIA_explanation.jpg :D"""

        k, N = data
        prob = 0.
        for i in range(N, 2 ** k + 1):
            prob += binom(2 ** k, i) * ((1 / 4) ** i) * ((3 / 4) ** (2 ** k - i))
        return prob
