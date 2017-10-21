import solution
import utils


class GC(solution.Solution):

    def _read(self, f):
        return utils.read_fasta(f)

    def solve(self, data):
        max_gc_id = None
        max_gc = 0

        for id_, dna in data:
            gc = sum([1 for i in dna if i == utils.CYTOSINE or i == utils.GUANINE]) * 1. / len(dna)
            if gc > max_gc:
                max_gc_id = id_
                max_gc = gc

        return max_gc_id, max_gc * 100

    def _write(self, f, answer):
        f.write('{}\n{}'.format(answer[0][1:], '%.6f' % answer[1]))
