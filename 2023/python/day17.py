import heapq

with open("input.txt") as f:
    grid = {(x, y): int(n) for y, line in enumerate(f.read().splitlines()) for x, n in enumerate(line)}

def sol(min_steps, max_steps):
    q = [(grid[(1, 0)], (1, 0), (1, 0), 0), (grid[(0, 1)], (0, 1), (0, 1), 0)]
    visited, end = set(), max(grid)
    while q:
        heat, (x, y), (dx, dy), steps = heapq.heappop(q)
        if (x, y) == end and min_steps <= steps:
            return heat
        if ((x, y), (dx, dy), steps) in visited:
            continue
        visited.add(((x, y), (dx, dy), steps))
        if steps < (max_steps - 1) and (x + dx, y + dy) in grid:
            s_pos = (x + dx, y + dy)
            heapq.heappush(q, (heat + grid[s_pos], s_pos, (dx, dy), steps + 1))
        if min_steps <= steps:
            lx, ly, rx, ry = dy, -dx, -dy, dx
            l_pos, r_pos = (x + lx, y + ly), (x + rx, y + ry)
            for xx, yy, pos in zip((lx, rx), (ly, ry), (l_pos, r_pos)):
                if pos in grid:
                    heapq.heappush(q, (heat + grid[pos], pos, (xx, yy), 0))

print(sol(0, 3), sol(3, 10))