import math


def main(fn):
    with open(fn) as f:
        presents = f.readlines()
    total = 0
    for present in presents:
        dimensions = [int(x) for x in present.split("x")]
        assert len(dimensions) == 3
        perimeter = sum(x + x for x in sorted(dimensions)[:2])
        cubic = math.prod(dimensions)
        total += perimeter + cubic
    print(total)


if __name__ == "__main__":
    main("input.txt")
