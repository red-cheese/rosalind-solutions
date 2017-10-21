import math
import solution


class ASPC(solution.SimpleWriteSolution):

    def _read(self, f):
        n, m = next(f).strip().split()
        return int(n), int(m)

    def solve(self, data):
        n, m = data
        answer = 0
        for k in range(m, n + 1):
            answer += (math.factorial(n) // math.factorial(k) // math.factorial(n - k))
            answer %= 1000000
        return int(answer)
