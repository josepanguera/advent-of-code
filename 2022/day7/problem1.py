from pathlib import Path


def main():
    with open("input.txt") as f:
        instructions = f.readlines()
    filesystem = parse_filesystem(instructions)
    total_size = find_dirs_under(filesystem, 100_000)
    print(total_size)


def parse_filesystem(lines):
    fs = {}
    cwd = Path("/")
    for line in lines:
        if line.startswith("$ cd "):
            line = line[len("$ cd "):].strip()
            cwd = (cwd / line).resolve()
            if cwd not in fs:
                fs[cwd] = {"dirs": [], "files": []}
        elif line.startswith("dir"):
            fs[cwd]["dirs"].append(cwd / line.strip().split()[-1])
        elif line.startswith("$ ls"):
            pass
        else:
            size, fn = line.strip().split()
            size = int(size)
            fs[cwd]["files"].append((size, fn))
    return fs


def find_dirs_under(filesystem, max_size):
    calculate_dir_size(filesystem, Path("/"))
    under_size = [dir_ for path, dir_ in filesystem.items() if dir_["size"] <= max_size]
    total_size = sum([dir_["size"] for dir_ in under_size])
    return total_size


def calculate_dir_size(filesystem, path):
    dir_ = filesystem[path]
    if "size" in dir_:
        return
    for sub_dir_path in dir_["dirs"]:
        calculate_dir_size(filesystem, sub_dir_path)
    size = sum(x[0] for x in dir_["files"])
    size += sum(filesystem[x]["size"] for x in dir_["dirs"])
    dir_["size"] = size


if __name__ == "__main__":
    main()
