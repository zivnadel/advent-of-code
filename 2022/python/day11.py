from dataclasses import dataclass
from math import prod

@dataclass
class Monkey:
    items: list[int]
    op: str
    div: int
    true: int
    false: int

def sol(part):
    res = 0
    with open("input.txt") as file:
        monkeys: list[Monkey] = []

        for i, monkey in enumerate(file.read().strip().split("\n\n")):
            lines = monkey.split("\n")
            monkeys.append(Monkey(
                [int(i.strip()) for i in lines[1].replace(":", ",").split(",") if i.strip().isnumeric()], 
                lines[2].split(" = ")[1], 
                int(lines[3].split()[-1]), 
                int(lines[4].split()[-1]),
                int(lines[5].split()[-1])
            ))

        k = prod(m.div for m in monkeys)
        insp = [0] * len(monkeys)

        for _ in range(20 if part == 1 else 10000):
            for i, monkey in enumerate(monkeys):
                for it in monkey.items:
                    insp[i] += 1
                    new = eval(monkey.op.replace("old", str(it)))
                    new = new // 3 if part == 1 else new % k
                    monkeys[monkey.true if new % monkey.div == 0 else monkey.false].items.append(new)
                monkey.items.clear()

        res = prod(sorted(insp)[-2:])

    return res

if __name__ == "__main__":
    print(sol(1), sol(2))
