#!/usr/bin/python

import argparse
import impl
import solution
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('id', metavar='ID', help='Problem ID (e.g. DNA)')
    parser.add_argument('-i', '--input', default='in.txt', help='Input file')
    parser.add_argument('-o', '--output', default='out.txt', help='Output file')
    args = parser.parse_args(sys.argv[1:])
    print(solution.Solution.go(args.id, args.input, args.output))


if __name__ == '__main__':
    main()
