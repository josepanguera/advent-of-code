from pathlib import Path
from typing import Any


DISK_SIZE = 70_000_000
NEEDED_SIZE = 30_000_000


def main():
    with open("input.txt") as f:
        instructions = f.readlines()
    filesystem = parse_filesystem(instructions)
    calculate_dir_size(filesystem, Path("/"))
    min_size = 30_000_000 - (70_000_000 - filesystem[Path("/")]["size"])
    sizes = [x["size"] for x in filesystem.values() if x["size"] >= min_size]
    sizes = sorted(sizes)
    print(sizes[0])


def parse_filesystem(lines) -> dict[Path, dict[str, Any]]:
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
