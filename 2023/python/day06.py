import re
import math

with open("input.txt") as f:
    time, dist = [list(map(int, re.findall(r"\d+", line))) for line in f.read().strip().splitlines()]

def sol():
    ways = []
    for i, race in enumerate(time):
        speeds = 0
        for j in range(race+1):
            speed = j * (race - j)
            if speed > dist[i]:
                speeds += 1
        ways.append(speeds)
    return math.prod(ways)

print(sol())