import solution
import utils


class GC(solution.Solution):

    _NAME = 'GC'

    @classmethod
    def _read(cls, f):
        dnas = []

        id_ = None
        dna = ''

        for line in f:
            line = line.strip()
            print(line)

            if line.startswith('>'):
                # Flush the old ID.
                if id_ is not None:
                    dnas.append((id_, dna))
                    dna = ''

                id_ = line
            else:
                dna += line

        # Flush the last one.
        if id_ is not None:
            dnas.append((id_, dna))

        return dnas

    @classmethod
    def _solve(cls, data):
        max_gc_id = None
        max_gc = 0

        for id_, dna in data:
            gc = sum([1 for i in dna if i == utils.CYTOSINE or i == utils.GUANINE]) * 1. / len(dna)
            if gc > max_gc:
                max_gc_id = id_
                max_gc = gc

        return max_gc_id, max_gc * 100

    @classmethod
    def _write(cls, f, answer):
        f.write('{}\n{}'.format(answer[0][1:], '%.6f' % answer[1]))
