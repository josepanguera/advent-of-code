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
    visited = {tuple(santa)}
    for direction in directions:
        santa = LEGEND[direction](santa)
        visited.add(tuple(santa))
    print(len(visited))


if __name__ == "__main__":
    main("input.txt")
