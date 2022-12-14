from collections import defaultdict

def sol(part):
    def move(x, y):
        for i, j in [(x, y + 1), (x - 1, y + 1), (x + 1, y + 1)]:
            if grid[(i, j)] not in 'o#' and (part == 1 or j != floor):
                return i, j
        return x, y

    grid = defaultdict(lambda: '.')
    for line in [x.strip() for x in open("input.txt").readlines()]:
        coords = list(map(lambda x: tuple(map(int, x.split(','))), line.split(' -> ')))
        for (px, py), (nx, ny) in zip(coords, coords[1:]):
            for i in range(min(px, nx), max(px, nx) + 1):
                for j in range(min(py, ny), max(py, ny) + 1):
                    grid[(i, j)] = '#'

    prev, floor = (500, 0), max(map(lambda x: x[1], grid.keys())) + 2
    while True:
        new = move(*prev)
        if new == prev:
            grid[new] = 'o'
            prev = (500, 0)
            if new == (500, 0):
                break
        else:
            if new[1] > floor:
                break
            prev = new

    return sum([x == "o" for x in grid.values()])

if __name__ == "__main__":
    print(sol(1))
    print(sol(2))
