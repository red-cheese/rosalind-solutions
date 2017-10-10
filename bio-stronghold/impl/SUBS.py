import solution


class SUBS(solution.Solution):

    _NAME = 'SUBS'

    @classmethod
    def _read(cls, f):
        lines = [line.strip() for line in f if line.strip()]
        assert len(lines) == 2
        return lines

    @classmethod
    def _solve(cls, data):
        s, t = data
        return [i + 1 for i in range(len(s)) if t == s[i:(i + len(t))]]

    @classmethod
    def _write(cls, f, answer):
        f.write(' '.join([str(i) for i in answer]))
