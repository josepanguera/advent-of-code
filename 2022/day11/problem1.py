class Monkey:
    def __init__(self, items, operation, test, monkey_true, monkey_false):
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = monkey_true
        self.if_false = monkey_false
        self.inspected = 0

    def play(self, monkeys):
        for item in self.items:
            item = self.operation(item)
            item = item // 3
            to = self.if_true if item % self.test == 0 else self.if_false
            monkeys[to].items.append(item)
            self.inspected += 1
        self.items = []


def main(rounds):
    with open("input.txt") as f:
        lines = f.readlines()
    monkeys = parse_monkeys(lines)
    for _ in range(rounds):
        play_round(monkeys)
    inspected = sorted(x.inspected for x in monkeys)
    top2 = inspected[-2:]
    monkey_business = top2[0] * top2[1]
    print(monkey_business)


def parse_monkeys(lines):
    def parse_items(s):
        return [int(x) for x in s.strip().split(":")[1].split(",")]

    def parse_operation(s):
        return eval("lambda old: " + s.strip()[len("Operation: new = ") :])

    monkeys = []
    for i in range(0, (len(lines) + 1) // 7):
        monkey = Monkey(
            parse_items(lines[i * 7 + 1]),
            parse_operation(lines[i * 7 + 2]),
            int(lines[i * 7 + 3].strip().split()[-1]),
            int(lines[i * 7 + 4].strip().split()[-1]),
            int(lines[i * 7 + 5].strip().split()[-1]),
        )
        monkeys.append(monkey)
    return monkeys


def play_round(monkeys):
    for monkey in monkeys:
        monkey.play(monkeys)


if __name__ == "__main__":
    main(20)
