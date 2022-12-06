def sol(length):
    res = 0
    with open("input.txt") as file:
        seq = file.read().strip()
        for i in range(len(seq)):
            if len(set(seq[i:i+length])) == length:
                res = i + length
                break
    return res

if __name__ == "__main__":
    print(sol(4), sol(14))
