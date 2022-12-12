from collections import namedtuple


Position = namedtuple("Position", ["x", "y"])


def main():
    with open("input.txt") as f:
        maze, start, end = parse_maze(f.readlines())
    steps = solve_maze(maze, start, end)
    print(steps)


def parse_maze(lines):
    maze = {}
    start = None
    end = None
    i = 0
    j = 0
    for i, line in enumerate(lines):
        for j, letter in enumerate(line.strip()):
            position = Position(i, j)
            maze[position] = letter
            if letter == "S":
                start = position
            elif letter == "E":
                end = position
    assert i != 0
    assert j != 0
    assert start is not None
    assert end is not None
    return maze, start, end


def solve_maze(maze, start, end):
    steps = 0
    solved = {end: steps}
    candidates = neighbours_with_access_to(end, maze, solved)
    while candidates:
        next_candidates = []
        for candidate in candidates:
            position, steps = candidate
            solved[position] = steps
            for next_candidate in neighbours_with_access_to(position, maze, solved):
                next_candidates.append(next_candidate)

        candidates = discard_solved_or_repeated(next_candidates, solved)
    return solved[start]


def neighbours_with_access_to(position, maze, solved):
    steps = solved[position] + 1
    up = Position(position.x, position.y - 1)
    if is_accessible(maze, up, position):
        yield up, steps
    down = Position(position.x, position.y + 1)
    if is_accessible(maze, down, position):
        yield down, steps
    right = Position(position.x - 1, position.y)
    if is_accessible(maze, right, position):
        yield right, steps
    left = Position(position.x + 1, position.y)
    if is_accessible(maze, left, position):
        yield left, steps


def is_accessible(maze, from_, to):
    if from_ not in maze:
        return False
    if maze[to] == "E":
        return maze[from_] == "z"
    if maze[from_] == "S":
        return True
    return (ord(maze[to]) - ord(maze[from_])) <= 1


def discard_solved_or_repeated(next_candidates, solved):
    candidates = {}
    for candidate in next_candidates:
        position, steps = candidate
        if position in solved:
            pass
        elif position not in candidates:
            candidates[position] = steps
        elif steps < candidates[position]:
            candidates[position] = steps
    return [(k, v) for k, v in candidates.items()]


if __name__ == "__main__":
    main()
