import solution
import utils


class KMP(solution.ArrayWriteSolution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)[0]

    def _solve(self, s):
        borders = [0] * len(s)

        for i in range(1, len(s)):
            b = borders[i - 1]
            while s[i] != s[b] and b > 0:
                b = borders[b - 1]

            if b == 0:
                borders[i] = 1 if s[0] == s[i] else 0
            else:
                assert s[i] == s[b]
                borders[i] = b + 1

        return borders
