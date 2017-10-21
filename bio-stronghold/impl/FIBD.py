import solution
import utils


class FIBD(solution.SimpleWriteSolution):

    def _read(self, f):
        n, m = utils.first_line(f).split()
        return int(n), int(m)

    def solve(self, data):
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
