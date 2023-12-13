with open("input.txt") as f:
    patterns = [l.splitlines() for l in f.read().split('\n\n')]


def mirror(pat, p):
    for i in range(1, len(pat[0])):
        if sum(sum(x != y for x, y in zip(l[:i][::-1], l[i:])) for l in pat) == p:
            return i
    return 0

print([sum(mirror(pat, p) + 100 * mirror(list(zip(*pat)), p) for pat in patterns) for p in (0, 1)])