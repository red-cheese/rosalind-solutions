import solution
import utils
from impl import DNA_RNA_REVC


class REVP(solution.Solution):

    _MIN_REVP_LEN = 4
    _MAX_REVP_LEN = 12

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)[0]

    def _is_revp(self, dna):
        return dna == DNA_RNA_REVC.REVC().solve(dna)

    def solve(self, data):
        revps_meta = []

        for l in range(self._MIN_REVP_LEN, self._MAX_REVP_LEN + 1):
            for i in range(0, len(data) - l + 1):
                block = data[i:(i + l)]
                if self._is_revp(block):
                    revps_meta.append((i + 1, l))

        return revps_meta

    def _write(self, f, answer):
        for pos, l in answer:
            f.write('{pos} {len}\n'.format(pos=pos, len=l))
