import solution
import utils


class PROT(solution.SimpleWriteSolution):

    _NAME = 'PROT'

    @classmethod
    def _read(cls, f):
        return utils.first_line(f)

    @classmethod
    def _solve(cls, data):
        assert len(data) % 3 == 0

        prot = ''

        for i in range(0, len(data), 3):
            codon = data[i:(i + 3)]
            amino_acid = utils.PROT_CODON_TABLE[codon]

            if amino_acid == -1:  # Stop codon
                return prot

            prot += amino_acid

        raise RuntimeError('Should have returned the result by now')


class PRTM(solution.SimpleWriteSolution):

    _NAME = 'PRTM'

    @classmethod
    def _read(cls, f):
        return utils.first_line(f)

    @classmethod
    def _solve(cls, data):
        return sum([utils.PROT_MASS_TABLE[aa] for aa in data])
