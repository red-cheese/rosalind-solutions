

class Solution:

    _IN = 'in.txt'
    _OUT = 'out.txt'

    @classmethod
    def _read(cls, f):
        raise NotImplementedError

    @classmethod
    def _solve(cls, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def _write(cls, f, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def __all_subclasses__(cls):
        for subclass in cls.__subclasses__():
            yield from subclass.__all_subclasses__()
            yield subclass

    @staticmethod
    def solve(name):
        cls = None
        for subcls in Solution.__all_subclasses__():
            if subcls.__name__ == name:
                cls = subcls
                break

        if cls is None:
            raise ValueError("Unknown task: '{}'".format(name))

        with open(cls._IN, 'r') as f:
            data = cls._read(f)
            answers = cls._solve(data)

        with open(cls._OUT, 'w') as f:
            cls._write(f, *answers)

        return answers


class SimpleWriteSolution(Solution):

    @classmethod
    def _write(cls, f, answer):
        f.write(str(answer))
