ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
DRAW = 3
LOSE = 0

OUTCOMES = {
    (ROCK, ROCK): DRAW,
    (ROCK, PAPER): WIN,
    (ROCK, SCISSORS): LOSE,
    (PAPER, ROCK): LOSE,
    (PAPER, PAPER): DRAW,
    (PAPER, SCISSORS): WIN,
    (SCISSORS, ROCK): WIN,
    (SCISSORS, PAPER): LOSE,
    (SCISSORS, SCISSORS): DRAW,
}

LEGEND = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}


def main(fn):
    with open(fn) as f:
        lines = f.readlines()
    score = 0
    for line in lines:
        opponent, me = line.strip().split(" ")
        opponent = LEGEND[opponent]
        me = LEGEND[me]
        score += me
        score += OUTCOMES[(opponent, me)]
    print(score)


if __name__ == "__main__":
    main("input.txt")
