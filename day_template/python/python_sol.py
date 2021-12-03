import sys
import argparse

def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", dest="file")
    parser.add_argument("-d", "--debug", action="store_true", dest="debug")

    args = parser.parse_args(argv[1:])

    default_file = "../debug" if args.debug else "../input"

    args.file = default_file if args.file is None else args.file

    contents = list()
    with open(args.file, 'r') as f:
        contents = f.readlines()

    # Part 1

    print("?")
    print(f"Answer: {1}")

    # Part 2

    print("?")
    print(f"Answer: {1}")


if __name__ == "__main__":
    main(sys.argv)
