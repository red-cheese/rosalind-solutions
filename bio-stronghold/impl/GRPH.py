import solution
import utils


class GRPH(solution.Solution):

    _K = 3

    def _read(self, f):
        return utils.read_fasta(f)

    def solve(self, data):
        adj_list = []

        # Register edges v1 -> v2.
        for v1_id, v1_dna in data:
            for v2_id, v2_dna in data:
                if v1_id == v2_id:
                    continue

                suffix = v1_dna[-self._K:]
                prefix = v2_dna[:self._K]
                if suffix == prefix:
                    adj_list.append((v1_id, v2_id))

        return adj_list

    def _write(self, f, answer):
        f.writelines(['{start} {end}\n'.format(start=v1_id, end=v2_id)
                      for v1_id, v2_id in answer])
