import solution


class LEXF(solution.Solution):

    def _read(self, f):
        alphabet = next(f).strip().split()
        n = int(next(f).strip())
        return alphabet, n

    def _choice(self, alphabet, n):
        if n == 0:
            raise ValueError
        if not alphabet:
            raise ValueError
        if n > len(alphabet):
            raise ValueError

        if n == 1:
            return alphabet

        res = []

        for c in alphabet:
            res.extend([c + rest
                        for rest in self._choice(alphabet, n - 1)])

        return res

    def solve(self, data):
        alphabet, n = data
        return self._choice(sorted(alphabet), n)

    def _write(self, f, answer):
        for s in answer:
            f.write(s + '\n')
