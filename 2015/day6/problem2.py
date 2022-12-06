import re


GRID_SIZE = 1_000
LEGEND = {
    "turn on": lambda x: x + 1,
    "turn off": lambda x: max(x - 1, 0),
    "toggle": lambda x: x + 2,
}


def main(fn):
    with open(fn) as f:
        lines = f.readlines()
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    for instruction in instructions(lines):
        apply_instruction(grid, instruction)
    print(count(grid))


def instructions(lines):
    regex = re.compile(r"^(.+) (\d+),(\d+) through (\d+),(\d+)$")
    for line in lines:
        m = regex.match(line)
        action, x1, y1, x2, y2 = m.groups()
        yield action, int(x1), int(y1), int(x2), int(y2)


def apply_instruction(grid, instruction):
    action, x1, y1, x2, y2 = instruction
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            grid[i][j] = LEGEND[action](grid[i][j])


def count(grid):
    return sum(sum(x) for x in grid)


if __name__ == "__main__":
    main("input.txt")
