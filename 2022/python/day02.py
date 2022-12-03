def part1():
    res = 0
    points = { "A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3 }
    with open("input.txt") as file:
        rounds = file.read().strip().split('\n')
        for round in rounds:
            op, me = round.split(" ")
            if points[me] == points[op]:
                res += points[me] + 3
            elif (points[me] - 1 == points[op]) or (points[me] == 1 and points[op] == 3):
                res += points[me] + 6
            else:
                res += points[me]
    return res

def part2():
    res = 0
    points = { "A": 1, "B": 2, "C": 3 }
    with open("input.txt") as file:
        rounds = file.read().strip().split('\n')
        for round in rounds:
            op, todo = round.split(" ")
            if todo == "Y":
                res += points[op] + 3
            elif todo == "X":
                res += points["C" if op == "A" else chr(ord(op) - 1)]
            else:
                res += points["A" if op == "C" else chr(ord(op) + 1)] + 6
    return res

if __name__ == "__main__":
    print(part1())
    print(part2())
