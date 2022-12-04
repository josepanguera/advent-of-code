def main(fn):
    elves = []
    with open(fn) as f:
        lines = f.readlines()
    current_elf = 0
    for line in lines:
        line = line.strip()
        if not line:
            elves.append(current_elf)
            current_elf = 0
            continue
        current_elf += int(line)
    elves.append(current_elf)
    print(sum(sorted(elves)[-3:]))


if __name__ == "__main__":
    main("input.txt")
