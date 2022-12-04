def sol():
    res1 = 0
    res2 = 0
    with open("input.txt") as file:
        for line in file:
            e1, e2 = line.split(",")
            start1, end1 = e1.split("-")
            start2, end2 = e2.split("-")
            start1, start2, end1, end2 = int(start1), int(start2), int(end1), int (end2)
            if((start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1)):
                res1 += 1
            if((start1 >= start2 and start1 <= end2) or (start2 >= start1 and start2 <= end1)):
                res2 += 1
    return res1, res2

if __name__ == "__main__":
    print(sol())

