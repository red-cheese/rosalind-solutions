import math
import solution
import utils


class PMCH(solution.SimpleWriteSolution):

    _NAME = 'PMCH'

    @classmethod
    def _read(cls, f):
        return utils.read_fasta(f, dna_only=True)[0]

    @classmethod
    def _solve(cls, data):
        if not data:
            return 0

        A = sum(1 for nb in data if nb == 'A')
        C = sum(1 for nb in data if nb == 'C')
        assert (A + C) * 2 == len(data)

        return math.factorial(A) * math.factorial(C)
