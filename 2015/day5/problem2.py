def main(fn):
    with open(fn) as f:
        lines = f.readlines()
    print(len([x for x in lines if is_good(x)]))


def is_good(text):
    conditions = [
        has_a_repeated_pair,
        has_separated_twins,
    ]
    return all(x(text) for x in conditions)


def has_a_repeated_pair(text):
    for i in range(len(text) - 1):
        pair = text[i : i + 2]
        if pair in text[i + 2 :]:
            return True
    return False


def has_separated_twins(text):
    return any(x[0] == x[2] for x in zip(text, text[1:], text[2:]))


if __name__ == "__main__":
    main("input.txt")
