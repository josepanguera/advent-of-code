def main(fn):
    with open(fn) as f:
        instructions = f.readlines()[0]
    floor = instructions.count("(") - instructions.count(")")
    print(floor)


if __name__ == "__main__":
    main("input.txt")
