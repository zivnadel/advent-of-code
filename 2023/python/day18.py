with open("input.txt") as f:
    instructions = [line.split() for line in f.read().splitlines()]

D = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1), '0': (1, 0), '1': (0, 1), '2': (-1, 0), '3': (0, -1)}

def sol(part):
    coord, vertices, length = (0, 0), [(0, 0)], 0
    for directions, steps, color in instructions:
        steps = int(steps) if part == 1 else int(color[2:-2], 16)
        directions, length = (directions, length + steps) if part == 1 else (color[-2], length)
        coord = coord[0] + D[directions][0] * steps, coord[1] + D[directions][1] * steps
        vertices.append(coord)
    return int(abs(sum((v1[0]+v2[0]) * (v1[1]-v2[1]) / 2 for v1, v2 in zip(vertices, vertices[1:]))) + length/2 + 1) # Shoelance

print(sol(1), sol(2))