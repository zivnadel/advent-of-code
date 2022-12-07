from collections import defaultdict
from itertools import accumulate

def sol(part):
    sizes = defaultdict(int)
    cwd = []

    with open("input.txt") as file:
        for line in file:
            items = line.split()
            if line.strip() == "$ cd ..":
                cwd.pop()
            elif line.startswith("$ cd"):
                cwd.append(items[-1])
            elif items[0].isnumeric():
                for path in accumulate(cwd, func=lambda a, b: a + "/" + b):
                        sizes[path] += int(items[0])

    return sum(size for size in sizes.values() if size <= 100000) if part == 1 else min(size for size in sizes.values() if size >= sizes["/"] - 40000000)

if __name__ == "__main__":
    print(sol(1), sol(2))
