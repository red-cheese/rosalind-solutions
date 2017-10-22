import solution

from impl import LCSQ


class SCSP(solution.Solution):

    def _read(self, f):
        return next(f).strip(), next(f).strip()

    def solve(self, data):
        s, t = data
        # Indices with regard to s and t.
        lcsq = LCSQ.LCSQ().solve((s, t), indices=True)
        answer = []

        print('LCSQ:', lcsq)

        prev_i, prev_j = -1, -1
        for i, j in lcsq:
            print('Add', 'i', i, 'prev i', prev_i)
            print('Add', 'j', j, 'prev j', prev_j)
            assert s[i] == t[j]
            print(s[(prev_i + 1):i])
            print(t[(prev_j + 1):j])
            answer.extend(s[(prev_i + 1):i])
            answer.extend(t[(prev_j + 1):j])
            answer.append(s[i])
            prev_i, prev_j = i, j
            print()
            print()

        # Final bit.
        answer.extend(s[(prev_i + 1):])
        answer.extend(t[(prev_j + 1):])

        return answer

    def _write(self, f, answer):
        f.write(''.join(answer))
