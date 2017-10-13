import solution


class LEXF(solution.Solution):

    @classmethod
    def _read(cls, f):
        alphabet = next(f).strip().split()
        n = int(next(f).strip())
        return alphabet, n

    @classmethod
    def _choice(cls, alphabet, n):
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
                        for rest in cls._choice(alphabet, n - 1)])

        return res

    @classmethod
    def _solve(cls, data):
        alphabet, n = data
        return cls._choice(sorted(alphabet), n)

    @classmethod
    def _write(cls, f, answer):
        for s in answer:
            f.write(s + '\n')
