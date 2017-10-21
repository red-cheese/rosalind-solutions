import solution
import utils
from impl import DNA_RNA_REVC
from impl import PROT_PRTM_MPRT_MRNA


class SPLC(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)

    def solve(self, data):
        dna, *introns = data

        i = 0
        res = ''
        while i < len(dna):
            intron_removed = False
            for intron in introns:
                if dna[i:].startswith(intron):
                    i += len(intron)
                    intron_removed = True
                    break

            if intron_removed:
                continue

            res += dna[i]
            i += 1

        return PROT_PRTM_MPRT_MRNA.PROT().solve(DNA_RNA_REVC.RNA().solve(res))
