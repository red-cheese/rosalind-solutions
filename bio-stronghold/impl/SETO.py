import solution


class SETO(solution.Solution):

    def _read(self, f):
        n = int(next(f).strip())
        A = eval(next(f).strip())
        B = eval(next(f).strip())
        return n, A, B

    def _write(self, f, answer):
        for s in answer:
            f.write(str(s) + '\n')

    def solve(self, data):
        n, A, B = data
        C = {i for i in range(1, n + 1)}
        return A | B, A & B, A - B, B - A, C - A, C - B
