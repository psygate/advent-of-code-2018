import pprint
from builtins import enumerate
from itertools import accumulate, cycle


def get_input():
    with open("input.txt") as f:
        return [x.strip() for x in f.readlines()]


def part1():
    inputs = get_input()
    twos = [x for x in inputs if any(y for y in x if x.count(y) == 2)]
    threes = [x for x in inputs if any(y for y in x if x.count(y) == 3)]
    print(twos)
    print(threes)
    print(len(twos) * len(threes))


def word_distance(word, word2):
    return sum(word_distance_list(word, word2))

def word_distance_list(word, word2):
    diffs = list()
    for i in range(min(len(word), len(word2))):
        if word[i] != word2[i]:
            diffs.append(1)
        else:
            diffs.append(0)

    diffs += [1 for x in range(abs(len(word) - len(word2)))]

    return diffs

def part2():
    inputs = get_input()
    allids = [x for x in inputs if any(y for y in x if x.count(y) == 2 or x.count(y) == 3)]

    for index, word in enumerate(allids):
        for index2, word2 in enumerate(allids[index + 1:]):
            if index == index2:
                continue

            dist = word_distance_list(word, word2)
            if sum(dist) == 1:
                common = "".join([char for index, char in enumerate(word) if dist[index] == 0])
                print(common)


if __name__ == '__main__':
    part1()
    part2()
