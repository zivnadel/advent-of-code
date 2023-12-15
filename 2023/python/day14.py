rotate = lambda platform: [*map(list, zip(*platform[::-1]))] # rotate clockwise 90
load = lambda platform: sum(i for row in platform for i, ch in enumerate(row[::-1], 1) if ch == 'O')
north = lambda platform: rotate(rotate(rotate(platform))) # make it north

with open("input.txt") as f:
    platform = north([list(line) for line in f.read().splitlines()])

def tilt(platform):
    for row in platform:
        for i, tile in enumerate(row):
            new = i
            if tile == 'O' and new and row[new-1] == '.':
                while new > 0 and row[new-1] == '.':
                    new-=1
                row[new], row[i] = row[i], row[new]
    return platform

def part2(platform):
    platform, cache, n = north(platform), {}, 1000000000
    for row in range(n):
        for _ in range(4): platform = tilt(rotate(platform))
        p = cache.get(str(platform))
        if p: return cache[(n-p) % (row-p) + (p-1)]
        cache.update({str(platform): row, row: load(rotate(platform))})

print(load(tilt(platform)), part2(platform))