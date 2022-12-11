def sol():
    x, crt = 1, [1]
    with open("input.txt") as file:
        for line in file:
            if line.startswith("addx"):
                crt.append(x)
                x += int(line[5:])
            crt.append(x)

    print(sum(i * crt[i-1] for i in [20, 60, 100, 140, 180, 220]))

    for y in range(6):
        for x in range(40):
            print("#" if x in [crt[40*y + x] - 1, crt[40*y + x], crt[40*y + x] + 1] else ".", end="")
        print()

if __name__ == "__main__":
    sol()
