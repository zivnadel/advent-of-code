from functools import cmp_to_key

def comp(left, right):
    if type(left) is list and type(right) is int:
        right = [right]
    if type(left) is int and type(right) is list:
        left = [left]
    if type(left) is int and type(right) is int:
        if left < right:
            return 1
        if left == right:
            return 0
        return -1
    if type(left) is list and type(right) is list:
        i = 0
        while i < len(left) and i < len(right):
            x = comp(left[i], right[i])
            if x in [-1, 1]:
                return x
            i += 1

        if i == len(left):
            if len(left) == len(right):
                return 0
            return 1
        return -1

def sol():
    res1, res2 = 0, 1
    with open("input.txt") as f:
        f = f.read().strip()
        parts1, parts2 = f.split("\n\n"), f.replace("\n\n", "\n").split("\n")

        # part 1
        for i, part in enumerate(parts1):
            left, right = map(eval, part.split("\n"))
            if comp(left, right) == 1:
                res1 += i + 1

        # part 2
        packets = list(map(eval, parts2))
        packets.extend([[[2]], [[6]]])
        packets = sorted(packets, key=cmp_to_key(comp), reverse=True)

        for i, packet in enumerate(packets):
            if packet == [[2]]:
                res2 *= i + 1
            if packet == [[6]]:
                res2 *= i + 1

    return res1, res2

if __name__ == "__main__":
    print(sol())
