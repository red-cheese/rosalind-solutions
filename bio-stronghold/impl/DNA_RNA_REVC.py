import solution
import utils


class DNA(solution.ArrayWriteSolution):

    def _read(self, f):
        return utils.first_line(f)

    def solve(self, data):
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

        return [a, c, g, t]


class RNA(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.first_line(f)

    def solve(self, data):
        dna = data
        return dna if not dna else dna.replace(utils.THYMINE, utils.URACIL)


class REVC(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.first_line(f)

    def solve(self, data):
        dna = data

        if not dna:
            return dna

        return ''.join([utils.DNA_COMPLEMENTS[n] for n in dna[::-1]])
