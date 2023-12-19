import re

with open("input.txt") as f:
    workflows, ratings = f.read().split('\n\n')
    rules = {id: [ins.split(':') if ':' in ins else ins for ins in wf.split(',')]
            for id, wf in re.findall('^(\w*)\{(.*?)\}', workflows, re.M)}

def part1():
    total = 0
    for rating in ratings.splitlines():
        (x, m, a, s), id = map(int, re.findall(r"\d+", rating)), "in"
        while id not in 'RA':
            for rule in rules[id][:-1]:
                if eval(rule[0]):
                    id = rule[1]
                    break
            else:
                id = rules[id][-1]
        total += x + m + a + s if id == 'A' else 0
    return total

print(part1())


                    

