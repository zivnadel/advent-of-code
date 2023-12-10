coords = N, S, E, W = (-1, 0), (1, 0), (0, 1), (0, -1)
d = {'|': (N, S), '-': (E, W), 'L': (N, E), 'J': (N, W), '7': (S, W), 'F': (S, E), '.': ()}

with open("input.txt") as f:
  grid = f.read().strip().splitlines()

x, y = next(((i, j) for i, s in enumerate(grid) for j, ch in enumerate(s) if ch == "S"), None)
q = [((x-dx, y-dy), 1) for dx, dy in coords if (dx, dy) in d[grid[x-dx][y-dy]]]
visited = {(x, y)}.union(elem[0] for elem in q)

while q:
  (x, y), part1 = q.pop(0)
  for (dx, dy) in d[grid[x][y]]:
    n = (x + dx, y + dy)
    if n not in visited:
      q.append((n, part1 + 1))
      visited.add(n)

part2 = 0
for i in range(len(grid)):
  above = False
  for j in range(len(grid[i])):
    if grid[i][j] in {'|', 'L', 'J'} and (i, j) in visited: above = not above
    if above and (i, j) not in visited: part2 += 1

print(part1, part2)