def main(fn):
    total = 0
    with open(fn) as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        pair1, pair2 = line.split(",")
        pair1 = to_set(pair1)
        pair2 = to_set(pair2)
        if pair1 & pair2:
            total += 1
    print(total)


def to_set(range_):
    range_ = [int(x) for x in range_.split("-")]
    assert len(range_) == 2
    return set(range(range_[0], range_[1] + 1))


if __name__ == "__main__":
    main("input.txt")
