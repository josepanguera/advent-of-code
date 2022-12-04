import string


lowers = {x: i + 1 for i, x in enumerate(string.ascii_lowercase)}
uppers = {x: i + 27 for i, x in enumerate(string.ascii_uppercase)}
priorities = dict(lowers, **uppers)


def main(fn):
    total = 0
    with open(fn) as f:
        lines = f.readlines()
    for line in lines:
        first = list(line[len(line) // 2 :])
        second = list(line[: len(line) // 2])
        repeated = set(first) & set(second)
        assert len(repeated) == 1
        repeated = repeated.pop()
        # print(f"{repeated} -> {priorities[repeated]}")
        total += priorities[repeated]
    print(total)


if __name__ == "__main__":
    main("input.txt")
