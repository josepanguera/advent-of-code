class Cpu:
    def __init__(self):
        self.clock = 0
        self.register_x = 1
        self.visited = set()
        self.signal_strength = 0

    def tick(self, cycles=1):
        for _ in range(cycles):
            self.clock += 1
            if (self.clock - 20) % 40 == 0:
                self.signal_strength += self.clock * self.register_x

    def noop(self):
        self.tick()

    def addX(self, value):
        self.tick(2)
        self.register_x += value

    def execute(self, instructions):
        for instruction in instructions:
            instruction = instruction.split()
            if instruction[0] == "noop":
                self.noop()
            elif instruction[0] == "addx":
                self.addX(int(instruction[1]))


def main():
    with open("input.txt") as f:
        instructions = f.readlines()
    cpu = Cpu()
    cpu.execute(instructions)
    print(cpu.signal_strength)


if __name__ == "__main__":
    main()
