import solution
import utils


class IPRB(solution.SimpleWriteSolution):

    _NAME = 'IPRB'

    @classmethod
    def _read(cls, f):
        line = utils.first_line(f)
        return line.split()

    @classmethod
    def _solve(cls, data):
        AA, Aa, aa = data
        AA = float(AA)
        Aa = float(Aa)
        aa = float(aa)
        total = AA + Aa + aa

        aa_aa = aa / total * (aa - 1) / (total - 1)
        Aa_aa = 2 * Aa * aa / total / (total - 1) * 0.5
        Aa_Aa = Aa / total * (Aa - 1) / (total - 1) * 0.25

        return 1 - aa_aa - Aa_aa - Aa_Aa
