def main():
    with open("input.txt") as f:
        lines = f.readlines()
    forest, height, width = parse_forest(lines)
    total = count_visible_trees(forest, height, width)
    print(total)


def parse_forest(lines):
    forest = {}
    i, j = 0, 0
    for i, line in enumerate(lines):
        for j, tree in enumerate(line.strip()):
            forest[(i, j)] = tree
    return forest, i + 1, j + 1


def count_visible_trees(forest, height, width):
    scores = []
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            score = scenic_score(forest, height, width, x, y)
            scores.append(score)
    return max(scores)


def scenic_score(forest, height, width, x, y):
    tree_height = forest[(x, y)]
    total_score = 1

    score = 0
    for tree in [forest[xx, y] for xx in reversed(range(0, x))]:
        score += 1
        if tree >= tree_height:
            break
    total_score *= score

    score = 0
    for tree in [forest[xx, y] for xx in range(x + 1, width)]:
        score += 1
        if tree >= tree_height:
            break
    total_score *= score

    score = 0
    for tree in [forest[x, yy] for yy in reversed(range(0, y))]:
        score += 1
        if tree >= tree_height:
            break
    total_score *= score

    score = 0
    for tree in [forest[x, yy] for yy in range(y + 1, height)]:
        score += 1
        if tree >= tree_height:
            break
    total_score *= score

    return total_score


if __name__ == "__main__":
    main()
