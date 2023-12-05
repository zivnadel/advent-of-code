from functools import reduce

with open("input.txt") as f:
    seeds, *maps = f.read().strip().split('\n\n')
    seeds = list(map(int, seeds.split()[1:]))

def part1():
    def search(s, m):
        _, *ranges = m.split('\n')
        for r in ranges:
            dest, src, c = map(int, r.split())
            if src <= s < src+c:
                return s-src+dest
        else:
            return s
        
    return min(reduce(search, maps, s) for s in seeds)

def part2():
    blocks, locations = [[list(map(int, line.split())) for line in m.splitlines()[1:]] for m in maps], []
    for i in range(0, len(seeds), 2):
        ranges, results = [(seeds[i], seeds[i + 1] + seeds[i])], []
        for m in blocks:
            while ranges:
                rstart, rend = ranges.pop()
                for target, mstart, r in m:
                    mend = mstart + r
                    offset = target - mstart
                    if mend <= rstart or rend <= mstart:
                        continue
                    if rstart < mstart:
                        ranges.append((rstart, mstart))
                        rstart = mstart
                    if mend < rend:
                        ranges.append((mend, rend))
                        rend = mend
                    results.append((rstart + offset, rend + offset))
                    break
                else:
                    results.append((rstart, rend))
            ranges = results
            results = []
        locations += ranges
    return min(location[0] for location in locations)

print(part1(), part2())