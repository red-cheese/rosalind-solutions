import math
import numpy as np
import solution
import utils


class PROB(solution.ArrayWriteSolution):

    def _read(self, f):
        dna = next(f).strip()
        gcs = [float(gc) for gc in next(f).strip().split()]
        return dna, gcs

    def _solve(self, data, logprob=True):
        dna, gcs = data
        res = []

        for gc in gcs:
            prob_gc = gc / 2
            prob_at = (1 - gc) / 2
            if logprob:
                p = sum([math.log(prob_at if nb == utils.A or nb == utils.T else prob_gc, 10)
                         for nb in dna])
            else:
                p = np.prod([prob_at if nb == utils.A or nb == utils.T else prob_gc
                             for nb in dna])
            res.append(p)

        return res
