import collections
import solution


class CONV(solution.Solution):

    def _read(self, f):
        # Store as regular arrays.
        s1 = [round(float(v), 5) for v in next(f).strip().split()]
        s2 = [round(float(v), 5) for v in next(f).strip().split()]
        return s1, s2

    def solve(self, data):
        s1, s2 = data
        print(s1)
        print(s2)
        diff_counts = collections.defaultdict(int)
        for v1 in s1:
            for v2 in s2:
                diff_counts[round(v1 - v2, 5)] += 1
        max_count = max(diff_counts.values())
        print(max_count)
        for diff, count in diff_counts.items():
            if count == max_count:
                return max_count, diff
        raise RuntimeError

    def _write(self, f, answer):
        f.write(str(answer[0]) + '\n')
        f.write(str(answer[1]))
