import solution
import DNA_RNA_REVC


_REVC = DNA_RNA_REVC.REVC()


class DBRU(solution.Solution):

    def _read(self, f):
        return {line.strip() for line in f}

    def solve(self, s):
        s.update({_REVC.solve(dna) for dna in s})
        edges = [(dna[:-1], dna[1:]) for dna in s]
        return sorted(edges)

    def _write(self, f, answer):
        for edge in answer:
            f.write('({}, {})\n'.format(*edge))
