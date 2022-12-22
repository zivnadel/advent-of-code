from z3 import Solver, Int, ArithRef, sat

def sol():
    tree = { name: node for name, node in [line.split(": ") for line in open("input.txt").read().splitlines()] }

    def evaluate(node):
        if isinstance(node, ArithRef): # instance of z3 operation
            return node
        if node.isdigit():
            return int(node)
        c1, op, c2 = node.split(" ")
        c1, c2 = evaluate(tree[c1]), evaluate(tree[c2])
        return eval(f"c1 {op} c2")

    part1, solver, tree["humn"] = int(evaluate(tree["root"])), Solver(), Int("humn")
    solver.add(evaluate(tree["root"].replace("+", "==")))

    return part1, solver.model()[tree["humn"]] if solver.check() == sat else None # only if satisfied

if __name__ == "__main__":
    print(sol())