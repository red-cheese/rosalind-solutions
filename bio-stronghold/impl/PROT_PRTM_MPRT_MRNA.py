import collections
import solution
import utils
from urllib import request


class PROT(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.first_line(f)

    def solve(self, data):
        assert len(data) % 3 == 0

        prot = ''

        for i in range(0, len(data), 3):
            codon = data[i:(i + 3)]
            amino_acid = utils.PROT_CODON_TABLE[codon]

            if amino_acid == -1:  # Stop codon
                return prot

            prot += amino_acid

        raise RuntimeError('Should have returned the result by now')


class PRTM(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.first_line(f)

    def solve(self, data):
        return sum([utils.PROT_MASS_TABLE[aa] for aa in data])


class MPRT(solution.Solution):

    _URL_FORMAT = 'http://www.uniprot.org/uniprot/{id}.fasta'
    _N_GLYCOLYSATION = [
        (True, ['N']),
        (False, ['P']),  # Not 'P'
        (True, ['S', 'T']),
        (False, ['P']),
    ]

    def _read(self, f):
        return [line.strip() for line in f]

    def _match(self, prot, pattern):
        """Match the beginning of the protein string with the given pattern."""

        if len(prot) < len(pattern):
            return False

        for i, (require, symbols) in enumerate(pattern):
            if ((require and prot[i] not in symbols)
                    or (not require and prot[i] in symbols)):
                return False

        return True

    def solve(self, data):
        # First extract protein strings.
        prots = []
        for id_ in data:
            url = self._URL_FORMAT.format(id=id_)
            response = request.urlopen(url).read().decode().strip()
            _,  *prot_parts = response.split('\n')
            prots.append((id_, ''.join(prot_parts)))

        # Then look for the motif.
        return [(id_,
                 [i for i in range(len(prot))
                  if self._match(prot[i:], self._N_GLYCOLYSATION)])
                for id_, prot in prots]

    def _write(self, f, answer):
        for id_, indices in answer:
            if indices:
                f.write('{id}\n{indices}\n'
                        .format(id=id_, indices=' '.join([str(i + 1) for i in indices])))


class MRNA(solution.SimpleWriteSolution):

    def _read(self, f):
        return utils.first_line(f)

    def solve(self, data):
        # Reverse the protein codon table (just counts are enough).
        num_codons = collections.defaultdict(int)
        for codon, aa in utils.PROT_CODON_TABLE.items():
            num_codons[aa] += 1

        opts = [num_codons[aa] for aa in data]
        opts.append(num_codons[-1])

        # Now compute the product mod 1M.
        res = 1
        for opt in opts:
            res = (res * opt) % 1000000

        return res
