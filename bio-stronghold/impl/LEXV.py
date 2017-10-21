import solution


class LEXV(solution.Solution):

    def _read(self, f):
        alphabet = next(f).strip().split()
        n = int(next(f).strip())
        return alphabet, n

    def _solve_helper(self, alphabet, l):
        assert l > 0

        if l == 1:
            return alphabet

        words = []

        for a in alphabet:
            # All words of length up to l starting with a.
            words.append(a)
            for w in self._solve_helper(alphabet, l - 1):
                words.append(a + w)

        return words

    def solve(self, data):
        alphabet, n = data
        return self._solve_helper(alphabet, n)

    def _write(self, f, answer):
        for word in answer:
            f.write(word + '\n')
