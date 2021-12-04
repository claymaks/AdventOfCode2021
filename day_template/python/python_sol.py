import sys
import argparse

import tree

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file")
    parser.add_argument("-d", "--debug", action="store_true", dest="debug")

    args = parser.parse_args(argv[1:])

    default_file = "../debug" if args.debug else "../input"

    args.file = default_file if args.file is None else args.file

    contents = list()
    with open(args.file, 'r') as f:
        contents = [line.replace('\n', '') for line in f.readlines()]

    # Part 1
    tree.solution(1, 1)

    # Part 2

    tree.solution(2, 1)


if __name__ == "__main__":
    main(sys.argv)
