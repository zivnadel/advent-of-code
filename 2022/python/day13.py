from functools import cmp_to_key

def comp(l, r):
    if type(l) == type(r) == int:
        return 0 if l == r else 1 if l < r else -1
    l, r = map(lambda x: [x] if type(x) == int else x, [l, r])

    for vr, vl in zip(r, l):
        if (res := comp(vr, vl)) != 0:
            return res

    return 0 if len(l) == len(r) else 1 if len(l) < len(r) else -1

def sol():
    res1 = 0
    with open("input.txt") as f:
        f = f.read().strip()
        parts1, parts2 = f.split("\n\n"), f.replace("\n\n", "\n").split("\n")

        for i, part in enumerate(parts1):
            left, right = map(eval, part.split("\n"))
            if comp(left, right) == 1:
                res1 += i + 1

        packets = sorted([[[2]], [[6]]] + list(map(eval, parts2)), key=cmp_to_key(comp), reverse=True)

    return res1, (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

if __name__ == "__main__":
    print(sol())
