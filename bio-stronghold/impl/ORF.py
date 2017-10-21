import solution
import utils
from impl import DNA_RNA_REVC


class ORF(solution.Solution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)[0]

    def _translate(self, rna):
        """Translate the RNA block starting with the start codon
        and without a stop codon."""

        return ''.join([utils.PROT_CODON_TABLE[rna[i:(i + 3)]]
                        for i in range(0, len(rna), 3)])

    def _solve_helper(self, rna):
        res = set()
        starts = []

        for i in range(0, len(rna) - len(rna) % 3, 3):
            codon = rna[i:(i + 3)]

            if codon == utils.PROT_START_CODON:
                starts.append(i)
                continue

            if utils.PROT_CODON_TABLE[codon] == -1 and starts:
                res.update([self._translate(rna[s:i]) for s in starts])
                starts = []

        return res

    def solve(self, data):
        rna = data.replace(utils.T, utils.U)
        rna_rc = DNA_RNA_REVC.REVC().solve(data).replace(utils.T, utils.U)

        res = self._solve_helper(rna)
        res.update(self._solve_helper(rna[1:]))
        res.update(self._solve_helper(rna[2:]))
        res.update(self._solve_helper(rna_rc))
        res.update(self._solve_helper(rna_rc[1:]))
        res.update(self._solve_helper(rna_rc[2:]))

        return res

    def _write(self, f, answer):
        f.write('\n'.join(answer))
