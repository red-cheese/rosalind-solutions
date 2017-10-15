

class Solution:

    def __init__(self, input, output):
        self._input = input
        self._output = output

    @property
    def input(self):
        return self._input

    @property
    def output(self):
        return self._output

    def _read(self, f):
        raise NotImplementedError

    def _solve(self, data):
        raise NotImplementedError

    def _write(self, f, answer):
        raise NotImplementedError

    @classmethod
    def __all_subclasses__(cls):
        for subclass in cls.__subclasses__():
            yield from subclass.__all_subclasses__()
            yield subclass

    @staticmethod
    def solve(name, input, output):
        cls = None
        for subcls in Solution.__all_subclasses__():
            if subcls.__name__ == name:
                cls = subcls
                break

        if cls is None:
            raise ValueError("Unknown task: '{}'".format(name))

        alg = cls(input, output)

        with open(alg.input, 'r') as f:
            data = alg._read(f)
            answer = alg._solve(data)

        with open(alg.output, 'w') as f:
            alg._write(f, answer)

        return answer


class SimpleWriteSolution(Solution):

    def _read(self, f):
        raise NotImplementedError

    def _solve(self, data):
        raise NotImplementedError

    def _write(self, f, answer):
        f.write(str(answer))


class ArrayWriteSolution(Solution):

    def _read(self, f):
        raise NotImplementedError

    def _solve(self, data):
        raise NotImplementedError

    def _write(self, f, answer, add_one=False):
        f.write(' '.join([str(i + 1 if add_one else i) for i in answer]))
