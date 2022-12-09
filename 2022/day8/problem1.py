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
    total = height * 2 + (width - 2) * 2
    for x in range(1, height - 1):
        for y in range(1, width - 1):
            if is_visible(forest, height, width, x, y):
                total += 1
    return total


def is_visible(forest, height, width, x, y):
    tree_height = forest[(x, y)]
    to_the_left = max([forest[xx, y] for xx in range(0, x)])
    if to_the_left < tree_height:
        return True
    to_the_right = max([forest[xx, y] for xx in range(x + 1, width)])
    if to_the_right < tree_height:
        return True
    to_the_top = max([forest[x, yy] for yy in range(0, y)])
    if to_the_top < tree_height:
        return True
    to_the_bottom = max([forest[x, yy] for yy in range(y + 1, height)])
    if to_the_bottom < tree_height:
        return True
    return False


if __name__ == "__main__":
    main()
