def sol():
    x, crt, p = 1, [1], 0
    with open("input.txt") as file:
        for line in file:
            if line.startswith("addx"):
                crt.append(x)
                x += int(line[5:])
            crt.append(x)

    print(sum(i * crt[i-1] for i in [20, 60, 100, 140, 180, 220]))

    for _ in range(6):
        for x in range(40):
            if x in [crt[p] - 1, crt[p], crt[p] + 1]:
                print("#", end="")
            else:
                print(".", end="")
            p += 1
        print()

if __name__ == "__main__":
    sol()
