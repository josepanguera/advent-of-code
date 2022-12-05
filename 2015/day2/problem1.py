def main(fn):
    with open(fn) as f:
        presents = f.readlines()
    total = 0
    for present in presents:
        l, w, h = [int(x) for x in present.split("x")]
        sides = (2 * l * w, 2 * w * h, 2 * h * l)
        area = sum(sides)
        total += area + (min(sides) // 2)
    print(total)


if __name__ == "__main__":
    main("input.txt")
