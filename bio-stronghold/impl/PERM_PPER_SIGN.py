import solution
import utils


class PERM(solution.Solution):

    def _read(self, f):
        return int(utils.first_line(f))

    def _solve_helper(self, numbers, sign=False):
        if len(numbers) == 0:
            raise ValueError

        if len(numbers) == 1:
            return [[-numbers[0]], [numbers[0]]]

        perms = []
        for i, n in enumerate(numbers):
            rest = numbers[:i] + numbers[(i + 1):]

            # Two passes so that the results are nicely arranged.
            perms_rec = self._solve_helper(rest, sign=sign)
            if sign:
                perms.extend([[-n] + perm for perm in perms_rec])
            perms.extend([[n] + perm for perm in perms_rec])

        return perms

    def solve(self, data):
        n = data
        return self._solve_helper([i for i in range(1, n + 1)])

    def _write(self, f, answer):
        f.write(str(len(answer)))
        f.write('\n')

        for perm in answer:
            f.write(' '.join([str(n) for n in perm]))
            f.write('\n')


class PPER(solution.SimpleWriteSolution):

    def _read(self, f):
        N, k = utils.first_line(f).split()
        return int(N), int(k)

    def solve(self, data):
        N, k = data
        P_Nk = 1

        # In general, it's just math.factorial(N) // math.factorial(N - k),
        # but we need modulo 1000000 here.
        for i in range(N, N - k, -1):
            P_Nk *= i
            P_Nk %= 1000000

        return P_Nk


class SIGN(solution.Solution):

    def _read(self, f):
        return int(utils.first_line(f))

    def solve(self, n):
        perms = PERM()._solve_helper(list(range(1, n + 1)), sign=True)
        return len(perms), perms

    def _write(self, f, answer):
        f.write(str(answer[0]) + '\n')
        for perm in answer[1]:
            f.write(' '.join([str(i) for i in perm]) + '\n')
