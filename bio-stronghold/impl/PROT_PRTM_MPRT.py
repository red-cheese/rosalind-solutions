import solution
import utils
from urllib import request


class PROT(solution.SimpleWriteSolution):

    _NAME = 'PROT'

    @classmethod
    def _read(cls, f):
        return utils.first_line(f)

    @classmethod
    def _solve(cls, data):
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

    _NAME = 'PRTM'

    @classmethod
    def _read(cls, f):
        return utils.first_line(f)

    @classmethod
    def _solve(cls, data):
        return sum([utils.PROT_MASS_TABLE[aa] for aa in data])


class MPRT(solution.Solution):

    _NAME = 'MPRT'

    _URL_FORMAT = 'http://www.uniprot.org/uniprot/{id}.fasta'
    _N_GLYCOLYSATION = [
        (True, ['N']),
        (False, ['P']),  # Not 'P'
        (True, ['S', 'T']),
        (False, ['P']),
    ]

    @classmethod
    def _read(cls, f):
        return [line.strip() for line in f]

    @classmethod
    def _match(cls, prot, pattern):
        """Match the beginning of the protein string with the given pattern."""

        if len(prot) < len(pattern):
            return False

        for i, (require, symbols) in enumerate(pattern):
            if ((require and prot[i] not in symbols)
                    or (not require and prot[i] in symbols)):
                return False

        return True

    @classmethod
    def _solve(cls, data):
        # First extract protein strings.
        prots = []
        for id_ in data:
            url = cls._URL_FORMAT.format(id=id_)
            response = request.urlopen(url).read().decode().strip()
            _,  *prot_parts = response.split('\n')
            prots.append((id_, ''.join(prot_parts)))

        # Then look for the motif.
        return [(id_,
                 [i for i in range(len(prot))
                  if cls._match(prot[i:], cls._N_GLYCOLYSATION)])
                for id_, prot in prots]

    @classmethod
    def _write(cls, f, answer):
        for id_, indices in answer:
            if indices:
                f.write('{id}\n{indices}\n'
                        .format(id=id_, indices=' '.join([str(i + 1) for i in indices])))
