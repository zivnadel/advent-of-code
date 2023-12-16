from collections import defaultdict

N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)

with open("input.txt") as f:
    grid = f.read().splitlines()

def energize(energized, beam, d):
    while 0 <= beam[0] < len(grid[0]) and 0 <= beam[1] < len(grid) and d not in energized[beam]:
        energized[beam].add(d)
        match grid[beam[1]][beam[0]]:
            case '/':
                d = (-d[1], -d[0])
            case '\\':
                d = (d[1], d[0])
            case '-' if d in (N, S):
                energize(energized, (beam[0]+1, beam[1]), E)
                d = W
            case '|' if d in (E, W):
                energize(energized, (beam[0], beam[1]+1), S)
                d = N
        beam = (beam[0] + d[0], beam[1] + d[1])
    return len(energized)

print(energize(defaultdict(set), (0, 0), E)) # Part 1  

beams = (
    [((x, 0), S) for x in range(len(grid[0]))] +
    [((0, y), E) for y in range(len(grid))] +
    [((x, len(grid)-1), N) for x in range(len(grid[0]))] +
    [((len(grid[0])-1, y), W) for y in range(len(grid))]
)
    
print(max(energize(defaultdict(set), beam, d) for beam, d in beams)) # Part 2