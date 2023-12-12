from functools import cache

with open("input.txt") as f:
    lines = f.read().splitlines()

@cache
def arrangements(springs, group):  
    if not group:
        return int(all(s != '#' for s in springs))
    if len(springs) < sum(group):
        return 0
    if springs[0] == '.': 
        return arrangements(springs[1:], group)

    here = (
        arrangements(springs[(group[0] + 1):], group[1:])
        if all(s != '.' for s in springs[:group[0]])
        and (len(springs) > group[0] and springs[group[0]] != '#' or len(springs) <= group[0])
        else 0
    )
    next = arrangements(springs[1:], group) if springs[0] == '?' else 0
    
    return here + next
  
part1, part2 = 0, 0
for l in lines:  
    springs, group = l.split()[0], tuple(map(int, l.split()[1].split(',')))
    part1 += arrangements(springs, group)
    part2 += arrangements(((springs + '?') * 5)[:-1], group * 5)
    
print(part1, part2)