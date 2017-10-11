import math
import solution
import utils


class PROB(solution.Solution):

    _NAME = 'PROB'

    @classmethod
    def _read(cls, f):
        dna = next(f).strip()
        gcs = [float(gc) for gc in next(f).strip().split()]
        return dna, gcs

    @classmethod
    def _solve(cls, data):
        dna, gcs = data
        res = []

        for gc in gcs:
            prob_gc = gc / 2
            prob_at = (1 - gc) / 2
            res.append(sum([math.log(prob_at if nb == utils.A or nb == utils.T else prob_gc, 10)
                            for nb in dna]))

        return res

    @classmethod
    def _write(cls, f, answer):
        f.write(' '.join([str(lprob) for lprob in answer]))
