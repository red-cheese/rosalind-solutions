import solution
import utils


class TRAN(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)

    def solve(self, data):
        transitions = 0
        transversions = 0

        s1, s2 = data

        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue

            if (c1 in utils.PURINES) ^ (c2 in utils.PURINES):
                transversions += 1
            else:
                transitions += 1

        return transitions * 1. / transversions
