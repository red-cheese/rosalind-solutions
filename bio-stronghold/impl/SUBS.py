import solution


class SUBS(solution.Solution):

    def _read(self, f):
        lines = [line.strip() for line in f if line.strip()]
        assert len(lines) == 2
        return lines

    def solve(self, data):
        s, t = data
        return [i + 1 for i in range(len(s)) if t == s[i:(i + len(t))]]

    def _write(self, f, answer):
        f.write(' '.join([str(i) for i in answer]))
