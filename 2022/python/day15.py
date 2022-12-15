import re

def load():
    sensors, beacons = [], set()
    for line in open('input.txt'):
        sx, sy, bx, by = map(int, re.findall(r'-?\d+', line))
        sensors.append((sx, sy, abs(sx - bx) + abs(sy - by)))
        beacons.add((bx, by))
    return sensors, beacons

def part1():
    (sensors, beacons), row, imp = load(), 2000000, set()
    for sx, sy, radius in sensors:
        dist = radius - abs(sy - row)
        if dist > 0:
            for i in range(dist + 1):
                if (sx + i, row) not in beacons:
                    imp.add(sx + i)
                if (sx - i, row) not in beacons:
                    imp.add(sx - i)
    return len(imp)

def part2():
    (sensors, _), lim = load(), 4000000
    for y in range(lim + 1):
        x, changed = 0, True
        while changed:
            changed = False
            for sx, sy, radius in sensors:
                dist = abs(sx - x) + abs(sy - y)
                if dist <= radius:
                    x = sx + radius - abs(sy - y) + 1
                    changed = True
        if x <= lim:
            return (lim * x + y)

if __name__ == '__main__':
    print(part1(), part2())
