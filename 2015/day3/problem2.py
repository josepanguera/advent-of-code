LEGEND = {
    "^": lambda x: [x[0], x[1] + 1],
    ">": lambda x: [x[0] + 1, x[1]],
    "v": lambda x: [x[0], x[1] - 1],
    "<": lambda x: [x[0] - 1, x[1]],
}


def main(fn):
    with open(fn) as f:
        directions = f.readlines()[0]
    santa = [0, 0]
    robot_santa = [0, 0]
    visited = {tuple(santa)}
    for i in range(len(directions) // 2):
        santa = LEGEND[directions[i * 2]](santa)
        robot_santa = LEGEND[directions[i * 2 + 1]](robot_santa)
        visited.add(tuple(santa))
        visited.add(tuple(robot_santa))
    print(len(visited))


if __name__ == "__main__":
    main("input.txt")
