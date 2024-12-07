grid, word = [line.strip() for line in open("input.txt")], "XMAS"
rows, cols, word_len = len(grid), len(grid[0]), len(word)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

print(sum(
    1 if 
    all(0 <= r + dr * i < rows and 0 <= c + dc * i < cols and 
        grid[r + dr * i][c + dc * i] == word[i] for i in range(word_len))
    else 0 for dr, dc in directions
    for c in range(cols)
    for r in range(rows)
))

part2 = lambda r, c: ((r - 1 < 0 or r + 1 >= rows or c - 1 < 0 or c + 1 >= cols) == False
                      and grid[r-1][c-1] + grid[r][c] + grid[r+1][c+1] in ["SAM", "MAS"]
                      and grid[r-1][c+1] + grid[r][c] + grid[r+1][c-1] in ["SAM", "MAS"])

print(sum(1 if part2(r, c) else 0 for r in range(rows) for c in range(cols)))