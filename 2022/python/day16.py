valves = {}

with open("input.txt") as f:
    for line in f:
        id, flow, tunnels = line.split()[1], line.split()[4].split('=')[1].replace(";", ""), line.strip().replace(" valve ", " valves ").split(" valves ")[-1].split(", ")
        valves[id] = { 'flow': int(flow), 'tunnels': tunnels, 'paths': {} }

sorted_rooms = sorted([x for x in list(valves.keys()) if valves[x]['flow'] != 0])

def bfs(start, end):
    depth = 1
    while True:
        next = set()
        for i in start:
            if i == end:
                return depth
            for j in valves[i]['tunnels']:
                next.add(j)
        start = next
        depth += 1

for i in sorted_rooms + ['AA']:
    for j in sorted_rooms:
        if j != i:
            valves[i]['paths'][j] = bfs(valves[i]['tunnels'], j)

def sol(part):
    max_pressure = 0
    def f(opened, flowed, cur_room, depth, elephant):
        nonlocal max_pressure
        max_pressure = max(max_pressure, flowed)
        if depth <= 0:
            return

        if cur_room not in opened:
            f(opened.union([cur_room]), flowed + valves[cur_room]['flow'] * depth, cur_room, depth - 1, elephant)
            if not elephant and part == 2:
                f(set([cur_room]).union(opened), flowed + valves[cur_room]["flow"] * depth, 'AA', 25, True)
        else:
            for i in [x for x in valves[cur_room]['paths'].keys() if x not in opened]:
                f(opened, flowed, i, depth - valves[cur_room]['paths'][i], elephant)

    f(set(['AA']), 0, 'AA', 29 if part == 1 else 25, False)
    return max_pressure

if __name__ == '__main__':
    print(sol(1), sol(2))
