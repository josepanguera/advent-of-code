import string


lowers = {x: i + 1 for i, x in enumerate(string.ascii_lowercase)}
uppers = {x: i + 27 for i, x in enumerate(string.ascii_uppercase)}
priorities = dict(lowers, **uppers)


def main(fn):
    total = 0
    with open(fn) as f:
        lines = f.readlines()
    for i, line in enumerate(lines[::3]):
        line1 = set(list(lines[i * 3 + 0].strip()))
        line2 = set(list(lines[i * 3 + 1].strip()))
        line3 = set(list(lines[i * 3 + 2].strip()))
        common = line1 & line2 & line3
        assert len(common) == 1
        total += priorities[common.pop()]
    print(total)


if __name__ == "__main__":
    main("input.txt")
