import re
import math

with open("input.txt") as f:
    lines = f.read().strip().splitlines()
    t1, d1 = [list(map(int, re.findall(r"\d+", line))) for line in lines]
    t2, d2 = [int(''.join(re.findall(r"\d+", line))) for line in lines]

def sol(time, dist):
    ways = []
    for r, d in zip(time, dist):
        speed = 0
        for j in range(r+1):
            if j * (r - j) > d:
                speed += 1
        ways.append(speed)
    return math.prod(ways)

print(sol(t1, d1), sol([t2], [d2]))
