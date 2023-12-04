with open("input.txt") as f:
    lines = f.read().strip().splitlines()

def sol():
    points, cards = 0, [1]*len(lines)
    for i, l in enumerate(lines):
        winning, you = [(lambda x: {n.strip() for n in (x.split(": ")[1].split() if ":" in x else x.split())})(p) for p in l.split(" | ")]
        matches = len(winning & you)
        points += 2 ** (matches-1) if matches else 0
        for j in range(matches):
            cards[i+j+1] += cards[i]
    return points, sum(cards)

print(sol())