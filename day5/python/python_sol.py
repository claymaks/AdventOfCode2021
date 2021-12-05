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

    _min = [0, 0]
    _max = [0, 0]

    counts = dict()
    for line in contents:
        start, end = line.split(' -> ')
        start = list(map(int, start.split(',')))
        end = list(map(int, end.split(',')))

        _min[0] = min(_min[0], min(start[0], end[0]))
        _min[1] = min(_min[1], min(start[1], end[1]))

        _max[0] = max(_max[0], max(start[0], end[0]))
        _max[1] = max(_max[1], max(start[1], end[1]))

        if start[0] != end[0] and start[1] == end[1]:
            direction = 1 if end[0] - start[0] >= 0 else -1
            for x in range(int(start[0]), int(end[0]) + direction, direction):
                counts[f"{x},{start[1]}"] = counts.get(f"{x},{start[1]}", 0) + 1
        elif start[1] != end[1] and start[0] == end[0]:
            direction = 1 if end[1] - start[1] >= 0 else -1
            for y in range(int(start[1]), int(end[1]) + direction, direction):
                counts[f"{start[0]},{y}"] = counts.get(f"{start[0]},{y}", 0) + 1

    overlap = 0
    for k, v in counts.items():
        if v > 1:
            overlap += 1

##    for y in range(_min[0], _max[0] + 1):
##        for x in range(_min[1], _max[1] + 1):
##            print(counts.get(f"{x},{y}", '.'), end='')
##        print()

    # At how many points do at least two lines overlap?
    tree.solution(1, overlap)

    # Part 2

    _min = [0, 0]
    _max = [0, 0]

    counts = dict()
    for line in contents:
        start, end = line.split(' -> ')
        start = list(map(int, start.split(',')))
        end = list(map(int, end.split(',')))

        _min[0] = min(_min[0], min(start[0], end[0]))
        _min[1] = min(_min[1], min(start[1], end[1]))

        _max[0] = max(_max[0], max(start[0], end[0]))
        _max[1] = max(_max[1], max(start[1], end[1]))

        direction_x = 1 if end[0] - start[0] > 0 else -1 if end[0] - start[0] < 0 else 0
        direction_y = 1 if end[1] - start[1] > 0 else -1 if end[1] - start[1] < 0 else 0

        x,y = start
        while x != end[0] or y != end[1]:
            counts[f"{x},{y}"] = counts.get(f"{x},{y}", 0) + 1
            x += direction_x
            y += direction_y
        counts[f"{x},{y}"] = counts.get(f"{x},{y}", 0) + 1

    overlap = 0
    for k, v in counts.items():
        if v > 1:
            overlap += 1

    # At how many points do at least two lines overlap?
    tree.solution(2, overlap)


if __name__ == "__main__":
    main(sys.argv)
