from collections import deque

def sol():
    def bfs(grid, start, end):
        visited, to_visit = set([start]), deque([(start, 0)])

        while to_visit:
            (x, y), count = to_visit.popleft()
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and (nx, ny) not in visited and grid[ny][nx] <= grid[y][x] + 1:
                    if (nx, ny) == end:
                        return count + 1
                    to_visit.append(((nx, ny), count + 1))
                    visited.add((nx, ny))

        return float("inf")

    with open("input.txt") as file:
        grid, starts = [list(line) for line in file.read().splitlines()], []
        for y, line in enumerate(grid):
            for x, ch in enumerate(line):
                if ch == "S":
                    start = (x, y)
                    grid[y][x] = ord("a")
                elif ch == "E":
                    end = (x, y)
                    grid[y][x] = ord("z")
                else:
                    if grid[y][x] == "a":
                        starts.append((x, y))
                    grid[y][x] = ord(ch)

    return bfs(grid, start, end), min([bfs(grid, s, end) for s in starts])

if __name__ == "__main__":
    print(sol())
