from itertools import combinations

with open("input.txt") as f:
    grid = [list(line) for line in f.read().splitlines()]

def sol(p):
    exp = 1 if p == 1 else 999999
    empty = list([i for i, line in enumerate(g) if all(c == '.' for c in line)] for g in (grid, zip(*grid)))
    galaxies = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#']
    galaxies = [tuple((g[i] + sum(exp for j in empty[i] if j < g[i])) for i in (0, 1)) for g in galaxies]
    return sum(abs(x1-x2) + abs(y1-y2) for (x1, y1), (x2, y2) in combinations(galaxies, 2)) # Manhattan

print(sol(1), sol(2))
