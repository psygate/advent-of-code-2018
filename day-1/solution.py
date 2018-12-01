import pprint
from builtins import enumerate
from itertools import accumulate, cycle


def part1():
    with open("input.txt") as f:
        print(sum([int(x) for x in f.readlines()]))


def part2():
    with open("input.txt") as f:
        changes = [int(x) for x in f.readlines()]

    freq = 0
    freqs = set()

    for change in cycle(changes):
        if freq in freqs:
            print(freq)
            return

        freqs.add(freq)
        freq += change


if __name__ == '__main__':
    part1()
    part2()
