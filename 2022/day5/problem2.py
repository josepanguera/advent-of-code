import re


def main(fn):
    with open(fn) as f:
        lines = f.readlines()
    cargo = parse_cargo(lines)
    for quantity, from_stack, to_stack in parse_instructions(lines):
        cargo[to_stack] += cargo[from_stack][-quantity:]
        cargo[from_stack] = cargo[from_stack][:-quantity]
    top = [x[-1:][0] for x in cargo]
    # print(cargo)
    # print(top)
    print("".join(top))


def parse_cargo(lines):
    cargo = []
    for line in lines:
        if line.startswith(" 1"):
            break
        line = f" {line}"
        for i in range(0, len(line) // 4):
            if len(cargo) < i + 1:
                cargo.append([])
            crate = line[i * 4 + 2]
            if crate == " ":
                continue
            cargo[i].append(crate)
    for i, stack in enumerate(cargo):
        cargo[i] = list(reversed(stack))
    return cargo


def parse_instructions(lines):
    for line in lines:
        if not line.startswith("move"):
            continue
        m = re.match(r"move (\d+) from (\d+) to (\d+)$", line)
        assert len(m.groups()) == 3
        quantity, from_stack, to_stack = m.groups()
        yield int(quantity), int(from_stack) - 1, int(to_stack) - 1


if __name__ == "__main__":
    main("input.txt")
