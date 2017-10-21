import solution
import utils


class KMER(solution.ArrayWriteSolution):

    _ALPHABET = [utils.A, utils.C, utils.G, utils.T]
    _ALPHABET_LEN = len(_ALPHABET)
    _K = 4

    def _read(self, f):
        return utils.read_fasta(f, dna_only=True)[0]

    def solve(self, data):
        answer = [0] * (self._K ** self._ALPHABET_LEN)

        for i in range(len(data) - self._K + 1):
            # K-mer index is this k-mer itself translated from the base
            # _ALPHABET_LEN numeral system to the base 10 one.
            kmer_idx = 0
            for j in range(self._K):
                kmer_idx += self._ALPHABET.index(data[i + j]) * (self._ALPHABET_LEN ** (self._K - j - 1))

            answer[kmer_idx] += 1

        return answer
