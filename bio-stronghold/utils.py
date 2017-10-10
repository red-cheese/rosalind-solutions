

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


def first_line(f):
    return next(f).strip()
