def main():
    with open("input.txt") as f:
        sequence = f.read()
    start = find_start_of_signal(sequence)
    print(start)


def find_start_of_signal(sequence):
    length = 4
    for i in range(len(sequence) - length):
        if len(set(sequence[i:i + length])) == length:
            return i + length


if __name__ == "__main__":
    assert find_start_of_signal("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert find_start_of_signal("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert find_start_of_signal("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert find_start_of_signal("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
    main()
