import solution
import utils


class SSEQ(solution.Solution):

    @classmethod
    def _read(cls, f):
        s, t = utils.read_fasta(f, dna_only=True)
        return s, t

    @classmethod
    def _solve(cls, data):
        s, t = data
        if not t or not s or len(t) > len(s):
            raise ValueError

        res = []

        print(s, t)

        i = 0
        for j in range(len(s)):
            print(i, j)
            if s[j] == t[i]:
                res.append(j)
                i += 1
                if i == len(t):
                    break

        assert i == len(t)

        return res

    @classmethod
    def _write(cls, f, answer):
        f.write(' '.join([str(pos + 1) for pos in answer]))
