def sol():
    with open("input.txt") as file:
        trees, visibles, max_score = [list(map(int, line)) for line in file.read().splitlines()], 0, 0

        for row in range(len(trees)):
            for col in range(len(trees[0])):
                tree, visible, score = trees[row][col], False, 1

                for i in range(col+1, len(trees[0])):
                    if trees[row][i] >= tree:
                        score *= i - col
                        break
                else:
                    score *= len(trees[0]) - 1 - col
                    visible = True

                for i in range(col-1, -1, -1):
                    if trees[row][i] >= tree:
                        score *= col - i
                        break
                else:
                    score *= col
                    visible = True

                for i in range(row+1, len(trees)):
                    if trees[i][col] >= tree:
                        score *= i - row
                        break
                else:
                    score *= len(trees) - 1 - row
                    visible = True

                for i in range(row-1, -1, -1):
                    if trees[i][col] >= tree:
                        score *= row - i
                        break
                else:
                    score *= row
                    visible = True

                if visible:
                    visibles += 1

                max_score = max(max_score, score)
    return visibles, max_score

if __name__ == "__main__":
    print(sol())

