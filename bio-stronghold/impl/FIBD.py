import solution
import utils


class FIBD(solution.Solution):

    _NAME = 'FIBD'

    @classmethod
    def _read(cls, f):
        n, m = utils.first_line(f).split()
        return int(n), int(m)

    @classmethod
    def _solve(cls, data):
        n, m = data

        if n == 0:
            return 1

        rabbits = [0] * m  # Number of rabbits born in each month
        rabbits[-1] = 1

        for month in range(1, n):
            t = sum(rabbits[:-1])
            rabbits[:-1] = rabbits[1:]
            rabbits[-1] = t

        return sum(rabbits)

    @classmethod
    def _write(cls, f, answer):
        f.write(str(answer))
