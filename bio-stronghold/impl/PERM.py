import solution
import utils


class PERM(solution.Solution):

    _NAME = 'PERM'

    @classmethod
    def _read(cls, f):
        return int(utils.first_line(f))

    @classmethod
    def _solve_helper(cls, numbers):
        if len(numbers) == 0:
            raise ValueError

        if len(numbers) == 1:
            return [numbers]

        perms = []
        for i, n in enumerate(numbers):
            rest = numbers[:i] + numbers[(i + 1):]
            for perm in cls._solve_helper(rest):
                perms.append([n] + perm)
        return perms

    @classmethod
    def _solve(cls, data):
        n = data
        return cls._solve_helper([i for i in range(1, n + 1)])

    @classmethod
    def _write(cls, f, answer):
        f.write(str(len(answer)))
        f.write('\n')

        for perm in answer:
            f.write(' '.join([str(n) for n in perm]))
            f.write('\n')
