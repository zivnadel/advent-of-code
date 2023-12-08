import re, itertools, math

with open("input.txt") as f:
    ins, lines = f.read().split("\n\n")
    nodes = {elem: re.findall(r"\w+", coords) for elem, coords in [l.split(" = ") for l in lines.splitlines()]}

def lookup(n, part):
    s = 0
    for ch in itertools.cycle(ins):
        n, s = nodes[n][0 if ch == "L" else 1], s + 1
        if part == 1 and n == "ZZZ" or part == 2 and n.endswith("Z"):
            return s

n = {node: nodes[node] for node in nodes if node.endswith("A")}
print(lookup("AAA", 1), math.lcm(*[lookup(node, 2) for node in n]))