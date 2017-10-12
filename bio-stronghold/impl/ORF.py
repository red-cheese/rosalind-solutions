import solution
import utils
from . import DNA_RNA_REVC


class ORF(solution.Solution):

    _NAME = 'ORF'

    @classmethod
    def _read(cls, f):
        return utils.read_fasta(f, dna_only=True)[0]

    @classmethod
    def _translate(cls, rna):
        """Translate the RNA block starting with the start codon
        and without a stop codon."""

        return ''.join([utils.PROT_CODON_TABLE[rna[i:(i + 3)]]
                        for i in range(0, len(rna), 3)])

    @classmethod
    def _solve_helper(cls, rna):
        res = set()
        starts = []

        for i in range(0, len(rna) - len(rna) % 3, 3):
            codon = rna[i:(i + 3)]

            if codon == utils.PROT_START_CODON:
                starts.append(i)
                continue

            if utils.PROT_CODON_TABLE[codon] == -1 and starts:
                res.update([cls._translate(rna[s:i]) for s in starts])
                starts = []

        return res

    @classmethod
    def _solve(cls, data):
        rna = data.replace(utils.T, utils.U)
        rna_rc = DNA_RNA_REVC.REVC._solve(data).replace(utils.T, utils.U)

        res = cls._solve_helper(rna)
        res.update(cls._solve_helper(rna[1:]))
        res.update(cls._solve_helper(rna[2:]))
        res.update(cls._solve_helper(rna_rc))
        res.update(cls._solve_helper(rna_rc[1:]))
        res.update(cls._solve_helper(rna_rc[2:]))

        return res

    @classmethod
    def _write(cls, f, answer):
        f.write('\n'.join(answer))
