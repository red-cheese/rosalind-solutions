import solution
from impl import PROB


class RSTR(solution.SimpleWriteSolution):

    def _read(self, f):
        N, x = next(f).strip().split()
        N, x = int(N), float(x)
        dna = next(f).strip()
        return N, x, dna

    def _solve(self, data):
        N, x, dna = data
        return 1 - (1 - PROB.PROB(None, None)._solve((dna, [x]), logprob=False)[0]) ** N
