import collections
import solution
import utils

import DNA_RNA_REVC
import HAMM


class CORR(solution.Solution):

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)

    def solve(self, data):
        counts = collections.defaultdict(int)
        for read in data:
            counts[read] += 1

        err = []
        corr = []
        for read, cnt in counts.items():
            if cnt == 1 and DNA_RNA_REVC.REVC().solve(read) not in counts:
                err.append(read)
            else:
                corr.append(read)

        answer = []

        print(err)

        for read_err in err:
            for read_corr in corr:
                read_err_revc = DNA_RNA_REVC.REVC().solve(read_err)
                read_corr_revc = DNA_RNA_REVC.REVC().solve(read_corr)

                if HAMM.HAMM().solve((read_err, read_corr)) == 1:
                    answer.append((read_err, read_corr))
                    break
                if HAMM.HAMM().solve((read_err, read_corr_revc)) == 1:
                    answer.append((read_err, read_corr_revc))
                    break
                if HAMM.HAMM().solve((read_err_revc, read_corr)) == 1:
                    answer.append((read_err_revc, read_corr))
                    break

        return answer

    def _write(self, f, answer):
        for err, corr in answer:
            f.write('{err}->{corr}\n'.format(err=err, corr=corr))
