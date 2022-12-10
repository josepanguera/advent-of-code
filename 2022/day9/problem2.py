from dataclasses import dataclass


UP = "U"
DOWN = "D"
RIGHT = "R"
LEFT = "L"


@dataclass
class Knot:
    x: int
    y: int

    def up(self):
        self.y += 1

    def down(self):
        self.y -= 1

    def right(self):
        self.x += 1

    def left(self):
        self.x -= 1

    def as_tuple(self):
        return self.x, self.y

    def follow(self, other):
        if self.is_touching(other):
            return
        if other.x > self.x:
            self.x += 1
        if other.x < self.x:
            self.x -= 1
        if other.y > self.y:
            self.y += 1
        if other.y < self.y:
            self.y -= 1

    def is_touching(self, other):
        dx = abs(self.x - other.x)
        dy = abs(self.y - other.y)
        return dx <= 1 and dy <= 1


class Rope:
    def __init__(self, length):
        self.knots = [Knot(0, 0) for _ in range(length)]
        self.head = self.knots[0]
        self.tail = self.knots[-1]
        self.visited = set()
        self.track_tail()

    def move(self, movement):
        direction, steps = movement.split(" ")
        steps = int(steps)
        move = {
            UP: Knot.up,
            DOWN: Knot.down,
            RIGHT: Knot.right,
            LEFT: Knot.left,
        }[direction]
        for _ in range(steps):
            move(self.head)
            for i, knot in enumerate(self.knots[:-1]):
                next_knot = self.knots[i + 1]
                next_knot.follow(knot)
            self.track_tail()

    def track_tail(self):
        self.visited.add(self.tail.as_tuple())


def main():
    with open("input.txt") as f:
        lines = f.readlines()
    rope = simulate_movements(lines)
    print(len(rope.visited))


def simulate_movements(lines):
    rope = Rope(10)
    for movement in lines:
        rope.move(movement)
    return rope


if __name__ == "__main__":
    main()
