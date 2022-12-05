def main(fn):
    with open(fn) as f:
        lines = f.readlines()
    print(len([x for x in lines if is_good(x)]))


def is_good(text):
    conditions = [
        contains_three_vowels,
        has_a_letter_repeated,
        does_not_contain_bad_strings,
    ]
    return all(x(text) for x in conditions)


def contains_three_vowels(text):
    return len([x for x in text if x in "aeiou"]) >= 3


def has_a_letter_repeated(text):
    return any(x[0] == x[1] for x in zip(text, text[1:]))


def does_not_contain_bad_strings(text):
    bad = ["ab", "cd", "pq", "xy"]
    return not any(x in text for x in bad)


if __name__ == "__main__":
    main("input.txt")
