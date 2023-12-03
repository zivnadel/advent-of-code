with open("input.txt") as f:
    lines = f.read().strip().splitlines()

def sol():
    part1, part2 = 0, 0
    for line in lines:
        game, data = line.split(": ")
        id, sets = game.split()[1], data.split("; ")
        red, green, blue = [set() for _ in range(3)]
        for game_set in sets:
            for ball in game_set.split(", "):
                num, color = ball.split()
                eval(color).add(int(num))
        if max(red) <= 12 and max(green) <= 13 and max(blue) <= 14:
            part1 += int(id)
        part2 += max(red) * max(green) * max(blue)
    return part1, part2

print(sol())      