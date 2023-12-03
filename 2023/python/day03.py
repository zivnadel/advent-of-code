import itertools
import re
import math
from collections import defaultdict

with open("input.txt") as f:
    lines = f.read().strip().splitlines()

def sol():
    part1, coords, parts = 0, list(itertools.product((-1, 0, 1), (-1, 0, 1))), defaultdict(list)
    symbols = {
        (i, j)
        for i, line in enumerate(lines)
        for j, ch in enumerate(line)
        if ch != "." and not ch.isdigit()
    }
    for i, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            num = int(match.group())
            boundaries = {
                (i + di, j + dj)
                for di, dj in coords
                for j in range(match.start(), match.end())
            }
            if symbols & boundaries:
                part1 += num
            for symbol in symbols & boundaries:
                parts[symbol].append(num)

    return part1, sum(math.prod(part) for part in parts.values() if len(part) == 2)

print(sol())