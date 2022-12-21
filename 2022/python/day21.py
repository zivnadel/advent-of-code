from z3 import Solver, Int, ArithRef, sat

def sol():
    tree = { name: node for name, node in [line.split(": ") for line in open("input.txt").read().splitlines()] }

    def evaluate(curr):
        if isinstance(curr, ArithRef): # instance of z3 operation
            return curr
        if curr.isdigit():
            return int(curr)
        c1, op, c2 = curr.split(" ")
        c1, c2 = evaluate(tree[c1]), evaluate(tree[c2])
        return eval(f"c1 {op} c2")

    res1, res2 = evaluate(tree["root"]), 0

    s, tree["humn"] = Solver(), Int("humn")
    s.add(evaluate(tree["root"].replace("+", "==")))
    assert s.check() == sat # satifsiable
    res2 = s.model()[tree["humn"]]

    return res1, res2

if __name__ == "__main__":
    print(sol())