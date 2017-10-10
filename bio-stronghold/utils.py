

ADENINE = 'A'
CYTOSINE = 'C'
GUANINE = 'G'
THYMINE = 'T'

URACIL = 'U'

DNA_COMPLEMENTS = {
    ADENINE: THYMINE,
    THYMINE: ADENINE,
    CYTOSINE: GUANINE,
    GUANINE: CYTOSINE
}


PROT_CODON_TABLE = {
    'UUU': 'F',      'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
    'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
    'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
    'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
    'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
    'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
    'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
    'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
    'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
    'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
    'UAA': -1,       'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
    'UAG': -1,       'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
    'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
    'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
    'UGA': -1,       'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
    'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G',
}


def first_line(f):
    return next(f).strip()
