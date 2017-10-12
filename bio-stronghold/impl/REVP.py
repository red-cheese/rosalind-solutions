import solution
import utils
from . import DNA_RNA_REVC


class REVP(solution.Solution):

    _NAME = 'REVP'

    _MIN_REVP_LEN = 4
    _MAX_REVP_LEN = 12

    @classmethod
    def _read(cls, f):
        return utils.read_fasta(f, dna_only=True)[0]

    @classmethod
    def _is_revp(cls, dna):
        return dna == DNA_RNA_REVC.REVC._solve(dna)

    @classmethod
    def _solve(cls, data):
        revps_meta = []

        for l in range(cls._MIN_REVP_LEN, cls._MAX_REVP_LEN + 1):
            for i in range(0, len(data) - l + 1):
                block = data[i:(i + l)]
                if cls._is_revp(block):
                    revps_meta.append((i + 1, l))

        return revps_meta

    @classmethod
    def _write(cls, f, answer):
        for pos, l in answer:
            f.write('{pos} {len}\n'.format(pos=pos, len=l))
