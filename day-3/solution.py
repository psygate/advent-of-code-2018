import pprint
from builtins import enumerate
from itertools import accumulate, cycle


def get_input():
    with open("input.txt") as f:
        return [x.strip() for x in f.readlines()]


class Claim:
    def __init__(self, arg: str):
        parts = arg.split(" ")
        self.id = int(parts[0][1:])
        self.x = int(parts[2].split(",")[0])
        self.y = int(parts[2].split(",")[1][:-1])
        self.width = int(parts[3].split("x")[0])
        self.height = int(parts[3].split("x")[1])
        self.xmax = self.x + self.width
        self.ymax = self.y + self.height

    def __repr__(self):
        return f"Claim({self.id}, ({self.x}, {self.y})-({self.width}, {self.height}))"


def part1():
    claims = [Claim(x) for x in get_input()]
    field = list(list(list() for y in range(1000)) for x in range(1000))

    assert len(field) == 1000
    assert all(len(x) == 1000 for x in field)

    for claim in claims:
        for x in range(claim.x, claim.xmax):
            for y in range(claim.y, claim.ymax):
                field[x][y].append(claim)

    print(len([y for x in field for y in x if len(y) >= 2]))


def part2():
    claims = [Claim(x) for x in get_input()]
    field = list(list(list() for y in range(1000)) for x in range(1000))

    assert len(field) == 1000
    assert all(len(x) == 1000 for x in field)

    for claim in claims:
        for x in range(claim.x, claim.xmax):
            for y in range(claim.y, claim.ymax):
                field[x][y].append(claim)

    available = set(claims)
    for claim in [claim for x in field for y in x if len(y) >= 2 for claim in y]:
        if claim in available:
            available.remove(claim)

    print(available)


if __name__ == '__main__':
    part1()
    part2()
