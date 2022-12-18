from networkx import grid_graph, node_connected_component, edge_boundary

def sol():
    cubes = frozenset(tuple(map(int, line.split(","))) for line in open("input.txt").read().splitlines())
    water = grid_graph(dim=[range(-1, max(max([x for x in cube]) for cube in cubes) + 2)] * 3)
    void = water.copy()
    void.remove_nodes_from(cubes)
    steam = node_connected_component(void, (-1, -1, -1))
    return sum(1 for _ in edge_boundary(water, cubes)), sum(1 for _ in edge_boundary(water, steam))

if __name__ == "__main__":
    print(sol())

