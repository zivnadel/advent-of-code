reports = [list(map(int, line.split())) for line in open("input.txt")]

safe = lambda r: 1 if all(0 < r[i+1] - r[i] <= 3 for i in range(len(r)-1)) \
                 or all(0 < r[i] - r[i+1] <= 3 for i in range(len(r)-1)) else 0

print(sum(safe(r) for r in reports), )
print(sum(1 if any(safe(r[:i] + r[i+1:]) for i in range(len(r))) else 0 for r in reports))