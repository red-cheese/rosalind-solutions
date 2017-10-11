import solution
import utils


class LCSM(solution.SimpleWriteSolution):

    _NAME = 'LCSM'

    _SEP = 'Z'  # Bigger than 'A', 'C', 'G', 'T'

    @classmethod
    def _read(cls, f):
        return utils.read_fasta(f, dna_only=True)

    @classmethod
    def _lcp(cls, strings):
        res = ''
        min_len = min([len(s) for s in strings])
        for i in range(min_len):
            if all([s[i] == strings[0][i] and s[i] != cls._SEP for s in strings]):
                res += strings[0][i]
            else:
                break
        return res

    @classmethod
    def _solve(cls, data):
        """Solve with a suffix tree + longest common prefix of len(data)
        consecutive suffixes.

        VERY inefficient - operating on strings in a stupid way.
        Operating just on indices would be wiser."""

        k = len(data)

        # Build a sorted suffix array.
        concat = cls._SEP.join(data) + cls._SEP
        suffixes = [concat[i:] for i in range(len(concat))]
        suffixes.sort()

        # Find the longest common prefix of K strings.
        max_lcp = ''
        for i in range(len(suffixes) - k):
            lcp = cls._lcp(suffixes[i:(i + k)])
            if len(lcp) > len(max_lcp):
                max_lcp = lcp

        return max_lcp
