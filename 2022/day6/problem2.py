def main():
    with open("input.txt") as f:
        sequence = f.read()
    start = find_start_of_signal(sequence)
    print(start)


def find_start_of_signal(sequence):
    length = 14
    for i in range(len(sequence) - length):
        if len(set(sequence[i:i + length])) == length:
            return i + length


if __name__ == "__main__":
    assert find_start_of_signal("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert find_start_of_signal("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert find_start_of_signal("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert find_start_of_signal("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert find_start_of_signal("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
    main()
