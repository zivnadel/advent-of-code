part = 1
l, r = zip(*[map(int, line.split()) for line in open("input.txt")])

print(sum(abs(a - b) for a, b in zip(sorted(l), sorted(r))) if part == 1 
      else sum(x * r.count(x) for x in set(l)))