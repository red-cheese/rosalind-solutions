import solution
import utils


class SSEQ(solution.Solution):

    def _read(self, f):
        s, t = utils.read_fasta(f, dna_only=True)
        return s, t

    def _solve(self, data):
        s, t = data
        if not t or not s or len(t) > len(s):
            raise ValueError

        res = []

        i = 0
        for j in range(len(s)):
            if s[j] == t[i]:
                res.append(j)
                i += 1
                if i == len(t):
                    break

        assert i == len(t)

        return res

    def _write(self, f, answer):
        f.write(' '.join([str(pos + 1) for pos in answer]))
