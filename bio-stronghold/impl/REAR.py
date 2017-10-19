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

            pair.append([int(i) for i in line.split()])

        return data

    def _iddfs(self, p1, p2, cur_d, max_d, cache):
        """Recursive iterative deepening DFS."""

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

    def _rev_dist(self, p1, p2):
        print(p1, p2)
        # Distance -> set of pairs that won't work.
        cache = {}
        for max_d in range(self._MAX_D):
            print(max_d)
            cache[max_d] = set()
            if self._iddfs(p1, p2, 0, max_d, cache):
                return max_d
        return -1

    def _solve(self, data):
        ans = []
        for p1, p2 in data:
            ans.append(self._rev_dist(p1, p2))
        return ans

# a = [8, 6, 7, 9, 4, 1, 3, 10, 2, 5]
# b = [8, 2, 7, 6, 9, 1, 5, 3, 10, 4]

# a = [3, 10, 8, 2, 5, 4, 7, 1, 6, 9]
# b = [5, 2, 3, 1, 7, 4, 10, 8, 6, 9]

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [3, 1, 5, 2, 7, 4, 9, 6, 10, 8]
#
# print('answer:', REAR(None, None)._rev_dist(a, b))




