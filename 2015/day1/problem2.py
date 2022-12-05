def main(fn):
    with open(fn) as f:
        instructions = f.readlines()[0]
    current_floor = 0
    for i, step in enumerate(instructions):
        direction = 1 if step == "(" else -1
        current_floor += direction
        if current_floor == -1:
            break
    else:
        raise Exception("Impossible")
    print(i + 1)


if __name__ == "__main__":
    main("input.txt")
