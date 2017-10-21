import random
import solution


class REAR(solution.ArrayWriteSolution):

    _MAX_D = 1000000

    def _read(self, f):
        data = []
        pair = []
        for line in f:
            line = line.strip()

            if not line:
                assert len(pair) == 2
                data.append(pair)
                pair = []
                continue

            pair.append([int(i) - 1 for i in line.split()])

        assert len(pair) == 2
        data.append(pair)

        return data

    def _iddfs(self, p1, p2, cur_d, max_d, cache):
        """Recursive iterative deepening DFS.
        It was my 1st approach to the problem."""

        if p1 == p2:
            return True

        if cur_d >= max_d:
            return False

        key = (tuple(p1), tuple(p2))
        if key in cache[max_d - cur_d]:
            return False

        ijs = [(i, j) for i in range(len(p1)) for j in range(i + 1, len(p1))]
        random.shuffle(ijs)

        for i, j in ijs:
            interval = p1[i:(j + 1)]
            p1[i:(j + 1)] = reversed(interval)

            new_key = (tuple(p1), tuple(p2))
            if new_key not in cache[max_d - cur_d - 1]:
                res = self._iddfs(p1, p2, cur_d + 1, max_d, cache)
                if res:
                    return True

                cache[max_d - cur_d - 1].add(new_key)

            p1[i:(j + 1)] = interval

        cache[max_d - cur_d].add(key)

        return False

    def _num_breakpoints(self, p):
        return sum(1 for i, j in zip(p[:-1], p[1:]) if abs(i - j) > 1)

    def _reverse(self, p, i, j):
        assert 0 <= i < j < len(p)
        p[i:(j + 1)] = reversed(p[i:(j + 1)])

    def _breakpoint_reversal_sort(self, p):
        """BreakPointReversalSort from
        http://bix.ucsd.edu/bioalgorithms/presentations/Ch05_Rearrangements.pdf

        My own heuristic that I came up with because of my laziness:

        The original BreakPointReversalSort often returns longer distances,
        because on each step we pick the first reversal that minimizes break points.
        Ideally we should examine all reversals that result in the same minimum
        number of bps - with a DFS for example.

        But I thought I'd just run this simple and fast alg 500 times shuffling
        all possible reversals each time - and choose the minimum answer.

                                    ¯\_(ツ)_/¯
        """

        dist = 0

        while self._num_breakpoints(p) > 0:
            # Choose one of the reversals minimizing bp.
            min_bp = self._num_breakpoints(p)
            best_i = None
            best_j = None

            ijs = [(i, j) for i in range(len(p)) for j in range(i + 1, len(p))]
            random.shuffle(ijs)

            for i, j in ijs:
                self._reverse(p, i, j)

                cur_bp = self._num_breakpoints(p)
                if cur_bp < min_bp:
                    min_bp = cur_bp
                    best_i = i
                    best_j = j

                self._reverse(p, i, j)

            # Perform the reversal.
            dist += 1
            if best_j is None and best_i is None:
                # Flip one increasing strip.
                last_bp_index = [idx + 1 for idx, (i, j) in enumerate(zip(p[:-1], p[1:])) if abs(i - j) > 1][-1]
                self._reverse(p, last_bp_index, len(p) - 1)
            else:
                assert best_i is not None and best_j is not None
                self._reverse(p, best_i, best_j)

        # We came to the decreasing sequence - one last flip.
        if p[-1] == 0:
            dist += 1

        return dist

    def _inverse(self, p):
        inv = [None] * len(p)

        for i, v in enumerate(p):
            inv[v] = i

        return inv

    def _dot(self, p1, p2):
        """Returns p1 * p2 = p1(p2)."""

        dot = [None] * len(p2)

        for i, v in enumerate(p2):
            dot[i] = p1[v]

        return dot

    def _rev_dist_iddfs(self, p1, p2):
        print(p1, p2)
        # Distance -> set of pairs that won't work.
        cache = {}
        for max_d in range(self._MAX_D):
            print(max_d)
            cache[max_d] = set()
            if self._iddfs(p1, p2, 0, max_d, cache):
                return max_d
        return -1

    def solve(self, data):
        answers = []
        for p1, p2 in data:
            print(p1, '->', p2)
            # p1 to p2 <=> inv(p2) * p1 <=> 1
            p2_inv = self._inverse(p2)

            min_ans = self._breakpoint_reversal_sort(self._dot(p2_inv, p1))
            # See the explanation of this hack above.
            for _ in range(500):
                ans = self._breakpoint_reversal_sort(self._dot(p2_inv, p1))
                if ans < min_ans:
                    min_ans = ans

            answers.append(min_ans)
        return answers


def _test():
    alg = REAR(None, None)

    # Number of breakpoints.
    p = [1, 9, 3, 4, 7, 8, 2, 6, 5]
    assert alg._num_breakpoints(p) == 5
    p = [0, 1, 9, 3, 4, 7, 8, 2, 6, 5, 10]
    assert alg._num_breakpoints(p) == 6

    p = [0, 2, 3, 1, 5, 4]
    p_inv = [0, 3, 1, 2, 5, 4]
    assert alg._inverse(p) == p_inv
    assert alg._inverse(p_inv) == p
    assert alg._dot(p, p_inv) == alg._dot(p_inv, p) == [0, 1, 2, 3, 4, 5]

    p1 = [0, 3, 1, 2, 5, 4]
    p2 = [0, 5, 2, 4, 1, 3]
    assert alg._dot(p1, p2) == [0, 4, 1, 5, 3, 2]

if __name__ == '__main__':
    _test()
