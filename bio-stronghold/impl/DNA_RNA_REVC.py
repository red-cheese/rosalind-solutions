import solution
import utils


class DNA(solution.Solution):

    @classmethod
    def _read(cls, f):
        return utils.first_line(f)

    @classmethod
    def _solve(cls, data):
        dna = data
        a, c, g, t = 0, 0, 0, 0

        if not dna:
            dna = ''

        for char in dna:
            if char == utils.ADENINE:
                a += 1
            elif char == utils.CYTOSINE:
                c += 1
            elif char == utils.GUANINE:
                g += 1
            elif char == utils.THYMINE:
                t += 1

        return a, c, g, t

    @classmethod
    def _write(cls, f, answer):
        a, c, g, t = answer
        f.write('{a} {c} {g} {t}'.format(a=a, c=c, g=g, t=t))


class RNA(solution.Solution):

    @classmethod
    def _read(cls, f):
        return utils.first_line(f)

    @classmethod
    def _solve(cls, data):
        dna = data
        return dna if not dna else dna.replace(utils.THYMINE, utils.URACIL)

    @classmethod
    def _write(cls, f, answer):
        f.write(answer)


class REVC(solution.Solution):

    @classmethod
    def _read(cls, f):
        return utils.first_line(f)

    @classmethod
    def _solve(cls, data):
        dna = data

        if not dna:
            return dna

        return ''.join([utils.DNA_COMPLEMENTS[n] for n in dna[::-1]])

    @classmethod
    def _write(cls, f, answer):
        f.write(answer)
