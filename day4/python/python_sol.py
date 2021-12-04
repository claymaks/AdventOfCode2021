import sys
import argparse

import numpy as np

def read_board(contents):
    boards = dict()

    guesses = [int(i) for i in contents[0].split(',')]

    fptr = 2
    board_num = 0
    while fptr < len(contents):
        boards[board_num] = []
        for i in range(5):
            boards[board_num].append([int(contents[fptr][i:i+3]) for i in range(0, len(contents[fptr]), 3)])
            fptr += 1
        boards[board_num] = np.vstack(boards[board_num])
        
        fptr += 1
        board_num += 1

    return guesses, boards


def check_win(guessed):
    solution = [1 for _ in range(5)]
    for num, guess in guessed.items():
        if solution in guess.tolist():
            return num, "H"
        if solution in guess.T.tolist():
            return num, "V"

    return -1, ""
        


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
    guesses, boards = read_board(contents)

    guessed = dict()
    for board in range(len(boards)):
        guessed[board] = np.vstack([[0 for _ in range(5)] for _ in range(5)])

    for n, guess in enumerate(guesses):
        for board in range(len(boards)):
            coords = zip(*np.where(boards[board] == guess))
            for x,y in coords:
                guessed[board][x,y] = 1

        # We can't win if there have been less than 5 total moves.
        if n < 4:
            continue

        board_won, direction = check_win(guessed)
        if board_won == -1:
            continue

        guess_won = None

        if direction == "V":
            guess_won = guessed[board_won].T
            board_won = boards[board_won].T
        else:
            guess_won = guessed[board_won]
            board_won = boards[board_won]
        
        break

        
    

    print("What will your final score be if you choose that board?")
    row_sum = np.sum(np.sum(board_won * (1 - guess_won)))
    print(f"Answer: {row_sum}x{guess} = {row_sum * guess}")

    # Part 2

    guesses, boards = read_board(contents)

    guessed = dict()
    for board in range(len(boards)):
        guessed[board] = np.vstack([[0 for _ in range(5)] for _ in range(5)])

    for n, guess in enumerate(guesses):
        for board in boards.keys():
            coords = zip(*np.where(boards[board] == guess))
            for x,y in coords:
                guessed[board][x,y] = 1

        # We can't win if there have been less than 5 total moves.
        if n < 4:
            continue

        board_won = 0
        while board_won != -1 and len(boards) > 1:
            board_won, direction = check_win(guessed)
            
            if board_won == -1:
                continue

            if len(boards) > 1:
                del boards[board_won]
                del guessed[board_won]

        board_won, direction = check_win(guessed)
        if board_won == -1:
            continue


        guess_won = None


        if direction == "V":
            guess_won = guessed[board_won].T
            board_won = boards[board_won].T
        else:
            guess_won = guessed[board_won]
            board_won = boards[board_won]
        
        break


        
    print("Once it wins, what would its final score be?")
    row_sum = np.sum(np.sum(board_won * (1 - guess_won)))
    print(f"Answer: {row_sum}x{guess} = {row_sum * guess}")


if __name__ == "__main__":
    main(sys.argv)
