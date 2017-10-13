import solution


class TREE(solution.SimpleWriteSolution):

    def _read(self, f):
        n = int(next(f))
        return n, [tuple(line.strip().split()) for line in f]

    def _solve(self, data):
        n, edges = data
        return n - len(edges) - 1
