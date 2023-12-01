import re

with open("input.txt") as f:
    part1 = f.read().strip()
    part2 = (
        part1.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )


def sol(part):
    return sum(int(x[0] + x[-1]) for x in [re.findall("\d", line) for line in part.split("\n")])

print(sol(part1))
print(sol(part2))
    

