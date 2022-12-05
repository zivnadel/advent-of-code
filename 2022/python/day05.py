def constructStacks(stacksStr):
    stacks = [[] for _ in range(int(stacksStr.split()[-1]))]
    lines = stacksStr.split("\n")
    for line in lines:
        i = 0
        for idx, letter in enumerate(line):
            if idx % 4 == 0:
                i += 1
            if letter.isupper():
                stacks[i-1].insert(0, letter)
    return stacks

def sol():
    res1 = ""
    res2 = ""
    with open("input.txt") as file:
        stacksStr, procedure = file.read().strip().split('\n\n')
        procedure = procedure.split("\n")
        stacks1 = constructStacks(stacksStr)
        stacks2 = constructStacks(stacksStr) 
        for line in procedure:
            numbers = list(map(int, [chunk for chunk in line.split(" ") if chunk.isnumeric()]))
            q, origin, dest = numbers[0], numbers[1]-1, numbers[2]-1
            for i in range(0, q):
                stacks1[dest].append(stacks1[origin].pop())
            stacks2[dest].extend(stacks2[origin][-1*q:])
            stacks2[origin] = stacks2[origin][:-1*q]
        res1 = "".join([stack.pop() for stack in stacks1])
        res2 = "".join([stack.pop() for stack in stacks2])
    return res1, res2

if __name__ == "__main__":
    print(sol())
