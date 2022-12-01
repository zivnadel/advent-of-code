def sol(part):
    res = 0;
    with open("input.txt") as input_file:
        elves = input_file.read().strip().split('\n\n')
        summed = []
        for elf in elves:
           summed.append(sum(map(int, elf.split('\n'))))
        if part == 1:
            res = max(summed)
        else:
            res = sum(sorted(summed)[-3:])
        return res

if __name__ == "__main__":
    print(sol(1))
    print(sol(2))
