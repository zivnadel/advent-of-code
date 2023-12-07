from collections import Counter

with open("input.txt") as f:
    hands = [line.split() for line in f.read().strip().splitlines()]

def sol():
    labels1, labels2 = [dict(zip(s, range(13))) for s in ('23456789TJQKA', 'J23456789TQKA')]

    def part1(hand):
        return sorted(Counter(hand[0]).values(), reverse=True), [labels1[c] for c in hand[0]]

    def part2(hand):
        if hand[0] == 'JJJJJ': 
            type = [5,]
        else:
            c = Counter(hand[0])
            jokers = c.pop('J', 0)
            type = sorted(c.values(), reverse=True)
            type[0] += jokers
        return type, [labels2[c] for c in hand[0]]
    
    return [sum(int(bid) * (i+1) for i, (_, bid) in enumerate(sorted(hands, key=part))) for part in (part1, part2)]

print(sol())