class Crt:
    def __init__(self):
        self.width = 40
        self.height = 6
        self.pixels = []
        for i in range(self.height):
            self.pixels.append([' ' for _ in range(self.width)])

    def blitz(self, clock, register_x):
        row = clock // self.width
        col = clock % self.width
        if abs(col - register_x) <= 1:
            self.pixels[row][col] = '#'

    def print(self):
        for row in self.pixels:
            print(''.join(row))


class Cpu:
    def __init__(self):
        self.clock = 0
        self.register_x = 1
        self.visited = set()
        self.crt = Crt()

    def tick(self, cycles=1):
        for _ in range(cycles):
            self.crt.blitz(self.clock, self.register_x)
            self.clock += 1

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
    cpu.crt.print()


if __name__ == "__main__":
    main()
