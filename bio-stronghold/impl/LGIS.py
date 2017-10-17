import solution
from impl import LCSQ


class LGIS(solution.ArrayWriteSolution):

    def _read(self, f):
        _ = next(f)
        return [int(i) for i in next(f).strip().split()]

    def _solve(self, data):
        """
        Longest increasing subsequence = longest common subsequence of data and sorted(data).
        Longest decreasing subsequence = -(longest common subsequence of -data and sorted(-data))."""

        increasing = LCSQ.LCSQ(self.input, self.output)._solve((data, sorted(data)))

        neg_data = [-i for i in data]
        decreasing = [-i for i in LCSQ.LCSQ(self.input, self.output)._solve((neg_data, sorted(neg_data)))]

        return increasing, decreasing
