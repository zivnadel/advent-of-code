def sol(num_knots):
    visited = set()
    with open("input.txt") as file:
        dirs = {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}
        knots = [[0, 0] for _ in range(num_knots)]

        for line in file:
            dir, dist = line.split()
            for _ in range(int(dist)):
                knots[0][0] += dirs[dir][0]
                knots[0][1] += dirs[dir][1]

                for i in range(1, num_knots):
                    move_x, move_y = knots[i][0] - knots[i-1][0], knots[i][1] - knots[i-1][1]

                    if move_x >= 2 or move_x <= -2 or move_y >= 2 or move_y <= -2:
                        move_x, move_y = max(-1, min(1, move_x)), max(-1, min(1, move_y))

                        knots[i][0] -= move_x
                        knots[i][1] -= move_y
                visited.add((knots[-1][0], knots[-1][1]))
    return len(visited)

if __name__ == "__main__":
    print(sol(2), sol(10))

