#!/usr/bin/python

import impl
import solution
import sys


def main(id_=None):
    if id_ is None and len(sys.argv) < 2:
        raise RuntimeError('Please provide problem ID')

    print(solution.Solution.solve(id_ or sys.argv[1]))


if __name__ == '__main__':
    main()
