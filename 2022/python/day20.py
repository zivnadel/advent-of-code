zero = lambda a: next(i for i, (_, num) in enumerate(a) if num == 0)

def mix(f, new):
    for num in f:
        old_i = new.index(num)
        new_i = (old_i + num[1]) % (len(new) - 1)
        del new[old_i]
        new.insert(new_i, num)

def sol():
    f = list(enumerate(map(int, open("input.txt").read().splitlines())))
    f1, f2 = f, [(i, num * 811589153) for i, num in f.copy()]
    new_1, new_2 = f1.copy(), f2.copy()
    mix(f1, new_1)
    for _ in range(10):
        mix(f2, new_2)
    return sum(new_1[(zero(new_1) + i) % len(new_1)][1] for i in [1000, 2000, 3000]), sum(new_2[(zero(new_2) + i) % len(new_2)][1] for i in [1000, 2000, 3000])
    
if __name__ == "__main__":
    print(sol())