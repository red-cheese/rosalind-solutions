import math
import solution
import utils


class MMCH(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)[0]

    def _solve(self, data):
        coeff = 1

        a = sum(1 for nb in data if nb == utils.A)
        u = sum(1 for nb in data if nb == utils.U)
        g = sum(1 for nb in data if nb == utils.G)
        c = sum(1 for nb in data if nb == utils.C)

        coeff *= math.factorial(max(a, u)) // math.factorial(min(a, u)) // math.factorial(abs(a - u))
        coeff *= math.factorial(max(g, c)) // math.factorial(min(g, c)) // math.factorial(abs(g - c))

        return coeff * math.factorial(min(a, u)) * math.factorial(min(g, c))
