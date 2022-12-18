from itertools import cycle
from collections import defaultdict

jetdir, jets = {"<": -1, ">": 1}, cycle(open("input.txt").read().strip())

rocks = cycle((
    ((0, 0), (1, 0), (2, 0), (3, 0)),
    ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
    ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
    ((0, 0), (0, 1), (0, 2), (0, 3)),
    ((0, 0), (1, 0), (0, 1), (1, 1)),
))


def translatex(rock, dx):
    for idx in range(len(rock)):
        rock[idx][0] += dx

def translatey(rock, dy):
    for idx in range(len(rock)):
        rock[idx][1] += dy

def checkwalls(rock, dx):
    for p in rock:
        if not (0 <= p[0]+dx <= 6):
            return False
    return True

def checkblock(rock, grid, dx, dy):
    for x, y in rock:
        if (x+dx, y+dy) in grid:
            return False
    return True

def prune(grid, top):
    for p in [p for p in grid if p[1] < top - 100]:
        grid.remove(p)

target, grid, top, idx, tracker, initial, divisor, amount, tgtidx = 1_000_000_000_000 - 1, set([(x, 0) for x in range(7)]), 0, -1, defaultdict(list), None, None, None, -1
tracker = defaultdict(list)

while True:
    idx += 1

    rock = [[x+2, y+top+4] for x, y in next(rocks)]
    while True:
        dir = jetdir[next(jets)]
        if checkwalls(rock, dir) and checkblock(rock, grid, dir, 0):
            translatex(rock, dir)
        if not checkblock(rock, grid, 0, -1):
            break
        translatey(rock, -1)
    grid.update([(x, y) for x, y in rock])
    top = max([p[1] for p in rock] + [top])
    prune(grid, top)

    if idx == 2021:
        print(top)

    if idx == tgtidx:
        mod = top - (initial + ((idx // divisor) - 1) * amount)
        part2 = initial + ((target // divisor) - 1) * amount + mod
        print(part2)
        break

    if divisor is not None:
        continue

    if idx != 0:
        tracker[idx] = [(top, top)]

    for i in [i for i in tracker if idx % i == 0]:
        tracker[i].append((top, top-tracker[i][-1][0]))
        if len(tracker[i]) > 3 and tracker[i][-1][1] == tracker[i][-2][1] == tracker[i][-3][1] == tracker[i][-4][1]:
            divisor, initial, amount = i, tracker[i][0][0], tracker[i][-1][1]
            tgtidx, tracker = idx + (target % divisor), None
            break
        elif len(tracker[i]) > 3 and tracker[i][-1][1] != tracker[i][-2][1]:
            del tracker[i]
