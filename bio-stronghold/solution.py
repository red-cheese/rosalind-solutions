

class Solution:

    _NAME = '_ABSTRACT'

    _IN = 'in.txt'
    _OUT = 'out.txt'

    @classmethod
    def _read(cls, f):
        raise NotImplementedError

    @classmethod
    def _solve(cls, data):
        raise NotImplementedError

    @classmethod
    def _write(cls, f, answer):
        raise NotImplementedError

    @staticmethod
    def solve(name):
        cls = None
        for subcls in Solution.__subclasses__():
            if subcls._NAME == name:
                cls = subcls
                break

        if cls is None:
            raise ValueError("Unknown task: '{}'".format(name))

        with open(cls._IN, 'r') as f:
            data = cls._read(f)
            answer = cls._solve(data)

        with open(cls._OUT, 'w') as f:
            cls._write(f, answer)

        return answer
