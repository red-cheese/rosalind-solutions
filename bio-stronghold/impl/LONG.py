import solution
import utils


class LONG(solution.SimpleWriteSolution):

    _NAME = 'LONG'

    @classmethod
    def _read(cls, f):
        return utils.read_fasta(f, dna_only=True)

    @classmethod
    def _overlap(cls, s1: str, s2: str):
        # Swap if needed so that s1 is shorter.
        if len(s1) > len(s2):
            (s1, s2) = (s2, s1)

        max_overlap = 0

        # Try suffixes.
        for i in range(1, len(s1)):
            #print('+', s2, s1[:i])
            if s2.endswith(s1[:i]):
                max_overlap = i
                ##print(i)

        # Try prefixes.
        for i in range(1, len(s1)):
            #print('-', s2, s1[-i:])
            if s2.startswith(s1[-i:]):
                max_overlap = max(max_overlap, i)
                ##print(max_overlap)

        #print('OL', s1, s2, max_overlap)

        return max_overlap, max_overlap * 1. / len(s2)

    @classmethod
    def _solve(cls, data):
        """Heuristic approach: choose the pair that overlaps the most
        (= kills the biggest % of its shortest member),
        glue the pair, repeat."""

        data = set(data)  # Remove duplicates, if any.

        while len(data) > 1:
            max_overlap, max_overlap_pc = 0, 0.
            max_r1, max_r2 = None, None

            for r1 in data:
                for r2 in data:

                    if r1 == r2:
                        continue

                    overlap, overlap_pc = cls._overlap(r1, r2)
                    if max_overlap_pc < overlap_pc or (max_r1 is None and max_r2 is None):
                        max_overlap, max_overlap_pc = overlap, overlap_pc
                        max_r1 = r1
                        max_r2 = r2

            if max_r1.startswith(max_r2[-max_overlap:]):
                r1r2 = max_r2[:(-max_overlap)] + max_r1
            else:
                assert max_r1.endswith(max_r2[:max_overlap])
                r1r2 = max_r1 + max_r2[max_overlap:]

            #print(max_r1)
            #print(max_r2)
            #print(r1r2)
            #print()

            data -= {max_r1, max_r2}
            data.add(r1r2)

        return list(data)[0]
