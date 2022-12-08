from math import floor

def part1():
    prio = { chr(i+96): i for i in range(1, 27) } | { chr(i+64): i+26 for i in range(1, 27) }
    res = 0
    with open("input.txt") as file:
        for line in file:
            types = set()
            for i in range(0, len(line)):
                if i < floor(len(line)/2):
                    types.add(line[i])
                elif line[i] in types:
                    res += prio[line[i]]
                    break
    return res

def part2():
    prio = { chr(i+96): i for i in range(1, 27) } | { chr(i+64): i+26 for i in range(1, 27) }
    res = 0
    with open("input.txt") as file:
        squads = file.read().strip().split('\n')
        squads = [squads[i:i+3] for i in range(0, len(squads), 3)]
        for squad in squads:
            same = (set(squad[0]) & set(squad[1]) & set(squad[2])).pop()
            res += prio[same]
    return res

if __name__ == "__main__":
    print(part1())
    print(part2())
