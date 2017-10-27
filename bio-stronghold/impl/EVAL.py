import solution

import PROB


_PROB = PROB.PROB()


class EVAL(solution.ArrayWriteSolution):

    def _read(self, f):
        n = int(next(f).strip())
        s = next(f).strip()
        gcs = [float(gc) for gc in next(f).strip().split()]
        return n, s, gcs

    def solve(self, data):
        n, s, gcs = data
        probs_s = _PROB.solve((s, gcs), logprob=False)
        # Sum the probabilities that s occurs as a substring in position 0, 1, 2, ...
        answers = [(n - len(s) + 1) * p for p in probs_s]
        return answers
