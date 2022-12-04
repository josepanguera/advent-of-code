ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
DRAW = 3
LOSE = 0

LEGEND = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": LOSE,
    "Y": DRAW,
    "Z": WIN,
}

I_SHOULD_PLAY = {
    (ROCK, DRAW): ROCK,
    (ROCK, WIN): PAPER,
    (ROCK, LOSE): SCISSORS,
    (PAPER, LOSE): ROCK,
    (PAPER, DRAW): PAPER,
    (PAPER, WIN): SCISSORS,
    (SCISSORS, WIN): ROCK,
    (SCISSORS, LOSE): PAPER,
    (SCISSORS, DRAW): SCISSORS,
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
        score += I_SHOULD_PLAY[(opponent, me)]
    print(score)


if __name__ == "__main__":
    main("input.txt")
