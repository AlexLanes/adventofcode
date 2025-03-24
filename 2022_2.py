class EncryptedRockPaperScissors:

    moves: list[tuple[str, str]]
    shape_score = {
        a: b
        for a, b in zip("XYZ", range(1, 4))
    }
    outcomes_score = {
        "X": { "B": 0, "A": 3, "C": 6 },
        "Y": { "C": 0, "B": 3, "A": 6 },
        "Z": { "A": 0, "C": 3, "B": 6 },
    }

    def __init__ (self, s: str) -> None:
        self.moves = [
            tuple(line.split(" ", 1))
            for line in s.split("\n")
        ]

    def move_score (self, move: tuple[str, str]) -> int:
        opponent, hand = move
        return self.shape_score[hand] + self.outcomes_score[hand][opponent]

    def total_score (self) -> int:
        return sum(
            self.move_score(move)
            for move in self.moves
        )

example = """A Y
B X
C Z"""
puzzle = """B X
B Z
B Z
A Y
B X
A Y
C Y
A Y
C X
B X
A Y
B Z
A Y
A X
B X
A Y
A Y
B Y
A Y
A Y
A Y
B Y
C Y
A Y
A Y
C X
B Z
B Z
C Z
B Z
A Y
A Y
B Z
A Y
B X
A Y
A Y
A Y
C Z
A Y
C Y
B X
A Y
A Y
A Y
B X
A X
B Y
B Z
A Y
A Y
A Y
B Z
A Y
A Y
B Y
B X
C Y
B Z
C Z
A Y
C X
B Z
A Z
C X
A Y
A Y
A Z
B Z
A Y
A Y
B Y
B Z
A Y
A Y
C X
B X
A Y
B Z
A Y
B Y
B Y
A Y
B Y
B Z
B X
B Y
B X
B Z
B Z
A Y
A Y
A Z
A X
A Y
B Z
A Y
B X
A X
A Y
B X
A X
A Z
B Z
A Y
A Y
A Y
B Z
A Y
B X
A Y
A Y
B Z
B Y
A X
C Y
C Y
A Y
B X
B X
B Z
B Z
B Y
B Y
B Z
B Z
B X
B Z
B Z
B Z
A Y
A Y
B Z
B Z
B X
A Y
C Z
B Z
B X
B Z
A X
A Y
B X
B X
A Y
B X
B Z
B Z
A Z
B Y
A Y
B X
A Y
C Y
B Y
A Y
A Y
B Y
B X
A Y
B X
B Z
A Y
B Z
B X
B X
A Y
A Y
B Z
A Z
B Z
C Z
B Z
C X
A Y
A Y
A Y
A Y
A Y
A Z
B Z
B Y
C Y
A X
C Y
A Y
A X
B Z
A Y
C Z
A Y
A Y
A Z
C Y
C Y
A Y
A Y
A Y
B Z
B Z
B X
B X
B Y
A Y
A X
B Z
B X
B Z
A Y
B Z
A X
B Z
A Y
A Y
B Z
A X
B Y
A Y
A Y
A Y
B X
A Y
C Z
B Y
B X
A Y
B Z
A Y
A Y
A Y
B Z
A Z
C Y
A Y
A Y
B Z
A Y
A Y
A Y
B Z
A Z
A Y
A Y
A Y
A Y
A Y
A Y
B X
A Y
B X
A Y
C Z
B Z
A Y
A Y
B Z
A Y
A Y
B Z
A Y
A Y
A Y
B Z
A Z
A Y
A Y
C Y
A Y
A Y
A Y
B Z
A Y
A Z
B Z
C Y
B Y
B Z
B Z
C X
A Y
A X
B Y
A Y
B Z
A X
B Y
C Y
B Z
A Y
A Y
B X
A Y
B Z
B Z
B X
B Z
A Y
A Y
A Y
A Y
A Y
A Y
B Y
A Y
A Y
A Y
A Y
A Y
B Z
A Y
A Y
A Y
A Y
A Y
B Y
B Y
A Y
A Z
A Y
A Y
A Y
B X
B Z
A X
A Z
A Y
B X
A Z
A Y
B X
A X
B X
A Y
A Y
B X
B X
A Y
B X
A Y
A Y
B Y
B Z
A Y
A Y
B Z
C X
B X
B Z
B Z
A Y
A X
A Y
A Y
C Y
A Y
B Z
C Y
C Y
A Y
A Y
B X
A Y
A Y
A Y
A Y
A X
A Y
B Y
B Z
A Y
B Z
B X
C Y
B Z
B X
B Z
A Y
A Y
A Z
A Y
C Y
B Z
A Y
A Y
B Y
B Z
B Z
A X
A Y
B Z
A Y
B X
A Y
A Y
B Z
B X
B Z
A Y
A Y
B Y
B Z
B X
A Y
B X
A Y
A Y
A Y
A Y
A Y
B Z
A Y
B Y
A Z
B X
B Z
B X
A Y
B X
A Y
B Y
B Y
A Y
C Z
C Y
A Y
B Z
B X
A Y
A Y
A Y
A Y
B Y
B Z
B Z
A Y
A Y
A Y
A Y
B X
A Y
B Y
B Z
A Y
B Z
B Z
B Z
A Y
B Z
B Z
B X
B Z
A Y
B Z
A Y
B X
B Z
A Y
A Y
A Y
C Y
B Z
C Z
A Y
B Z
C Y
A Y
A Y
A Y
B Z
A Y
A Y
B X
B X
A X
A Y
A Y
B X
B X
A X
A Y
A Y
A X
B X
B Y
A Y
A Y
B X
B Z
B X
A Y
B X
B Y
A Y
B Y
B X
A Z
A Y
A Y
B X
A X
A Z
B X
A Y
A X
B X
A Y
A Y
A Y
A Y
A Y
B Y
A Y
B X
B Y
B Z
B Y
A Y
A Y
A Y
A Y
B Y
A Y
A X
B Y
A Y
B Z
A Y
A Z
A Y
A Y
A Y
C Z
A Y
A Y
B X
B X
C Z
A Y
B Z
A X
B X
A Y
B Z
A Y
B Z
A Y
A Y
B Z
A X
A X
B X
B Y
B Z
B Z
C Z
A Y
A X
A Y
C X
A Y
B X
B X
B Z
A Y
A Z
A Y
C Z
B Z
B Y
B Z
C Y
C X
A Y
B X
B Z
A Y
B X
B Y
A Y
A Y
A Y
A Y
B Z
C Y
B Y
C X
A Y
A Y
B Z
C Y
B Z
A Y
A X
A Y
A Y
A Y
A Y
B X
C Y
A Y
A Y
B X
A Y
B X
B Y
C Z
A Y
A Y
A Y
A Y
B Z
B X
C Y
B X
A Y
A Z
C Y
A X
A Y
B Z
B Z
A Y
A Y
C Y
A Y
B X
C Z
B Z
A X
A Y
A Y
B Z
B Z
A Y
B X
B X
B X
A Y
B X
B Z
A Y
A Y
A Y
A Y
C Y
A Y
C Z
A X
B Z
B X
A Y
B X
A Y
B Y
A Y
A Z
A Y
A Y
B Z
B Y
B X
B Z
A Y
A Y
A Y
A Y
A Y
A Y
A Y
A Y
C Z
B Z
B X
A Y
A Z
B Y
A Y
A Y
B Y
A Y
B Y
B X
A Y
A Z
A Y
A Y
A Y
A Y
A Z
A Y
B Z
A Y
A Y
B Z
B Z
A Y
C Z
B X
A Y
C Y
B X
A Y
B X
B Z
B Z
A Y
A Y
A Y
A X
B X
B X
A Y
B Y
B Y
A Y
A X
A Y
B Z
C Y
A Y
C Z
B Z
C Y
B X
A Z
A Y
A Y
A Y
A Y
C X
B X
B X
A Z
B Y
A Y
A Y
B X
A Y
A Y
A X
B X
C Z
B X
C Y
A X
B X
C Y
C X
A Y
A Y
B Y
C Y
A Y
B X
B Z
A X
A Y
B X
B Z
B Z
B X
B Z
B Y
A Y
A Y
A Y
A Y
A Y
A Z
B Y
A X
B X
C Y
A Y
B Y
A Y
B X
A Y
A Y
A Y
A Y
A Y
A Y
B Z
B Z
A Y
A Y
A Y
C Z
A Y
A Y
A Z
B Z
C Y
B Z
A Y
B Z
A X
A Y
B X
B Z
A Y
A Y
A Y
A Y
B X
B Y
C Z
A Y
A Y
A Y
C Z
A X
B Z
B X
C Y
B X
B X
A Y
C Y
B X
A Z
A Y
B X
A Y
A Y
B Z
A Y
A Y
A Y
B Y
A Y
A Y
A Y
A Y
B X
C Y
A Y
A Y
A Y
A Y
A Y
B Z
B X
B Z
A Y
B X
A Y
B X
C Y
A Y
A Y
A Y
C Y
A Z
A Y
A Y
B Y
B Z
B Z
A Y
B X
A Y
B X
C Y
A Y
B X
B X
B X
A Y
B Y
A Y
A Y
B X
B X
A Y
A Y
C Y
A Y
B Z
A Y
A Y
B Z
A Y
C Y
B X
A Y
A Y
A Y
B X
B X
B X
A Y
B Z
B Z
B X
B Z
A Y
B X
B Z
A Y
A Y
C Z
B X
B X
C Z
C Y
A Y
C Z
A Y
A X
B Z
A Y
A Y
A Y
B Z
B Z
B Z
A Y
A Y
B Z
C Y
A Y
A X
B Z
A Y
A Y
B Z
B Z
C Y
C Z
A Y
A X
B Z
C Z
B Y
B X
B X
B X
B Y
B X
A Y
B X
B Z
B Z
A Y
B Z
A Y
A Y
A Y
B X
A Y
A Y
B X
A Y
A Y
A Y
A Y
A Z
B X
A Y
B Z
A Y
A Y
B Z
A Y
A Y
A Y
A X
A Z
A Y
B Y
C Y
A Y
A Y
A Y
C Y
A Y
B X
A Y
B Z
B X
B Z
A Y
B Z
A Z
B X
A Y
A Z
B X
B X
B Z
A Y
A Y
B Z
A Z
A Y
C Y
A Y
A Y
B Z
B Z
B X
C Y
B X
A Y
B X
B Y
B Y
C Z
A Y
A Y
B Z
B X
A Y
A X
A Y
A Z
A Y
B Y
A X
A Y
B Y
A Y
B X
A Y
A Y
A Y
A Y
B Z
A Y
A Y
A Y
B X
A Y
B Y
A Y
A Y
B X
B Y
B X
B Z
A X
A Y
B X
B Z
A Y
B Y
B Y
A X
C Y
B Z
B X
A Y
B Z
A X
B Y
B X
A Y
C Y
B Z
B X
A Y
B Z
C Z
A Y
A Y
A Y
A Y
B X
B X
A X
A Y
A Y
A Y
A X
C Y
C X
B Z
A Y
A Y
B X
A Y
A Y
C Y
B X
A X
B X
C X
A Z
A Y
C Z
A Y
A Y
B Z
B Z
C Y
A Y
A Y
B X
B X
A Y
C X
A X
A Y
A Y
A Y
B Y
A Y
A Y
B X
A Y
B Z
C X
A Y
B X
A Y
A X
A Y
A X
B X
A Y
A Y
A Y
B Y
B Z
B Z
B X
B Z
A Y
B Z
A Y
B Z
C Z
A Z
A Z
B X
A X
B Z
B Z
A X
B X
C X
C X
A X
A Y
A X
B Z
C Y
B X
B Z
B X
A Y
A Y
A Y
B X
B Z
B Z
B Z
A Y
A Y
B Y
B Z
A Y
A Y
C Y
A Y
A X
A Y
A Y
A Y
B Z
B Z
A Y
B X
A Y
A Y
A Y
A Y
A X
A Y
B Z
A Y
A Y
B Z
A Y
A Y
A Y
B X
A Y
C Y
B X
A Y
A X
A Y
B Z
B Z
B Z
B Z
B Z
A Z
B Z
A Z
C Y
B X
B Y
A X
B X
B X
A Y
A Y
A Y
A Y
B Y
A Y
A Y
A X
A Y
B Y
B X
C Y
B X
C X
A Y
B Z
A Y
A Y
B Z
A Y
A Y
B X
A Y
C Y
A Y
A Y
A Y
C Z
A X
B Y
A Y
C Y
A Y
B Z
A Y
B Z
B X
A Y
A Y
C Y
A Y
B Y
B Z
A Y
B X
A Y
A Y
C Y
C X
A Y
B Z
A Y
B X
B Z
B X
B X
A Y
A Z
B X
A Z
A Y
C Y
B Y
B X
A Y
A Y
A Y
B X
B Z
B Y
B X
A Y
A Y
A Y
A Y
A X
A Y
B X
A Y
B Z
B Z
B X
A Y
A Y
C X
B Z
B Z
B Y
A Z
B Y
B Y
C Z
A X
B X
B X
A Y
A Y
B X
A Y
B Z
B X
B X
C X
B Z
A Y
A Y
B X
B Z
A Y
B Y
A Y
B X
B X
B X
B Y
A Y
B Z
A Y
B Y
B Z
B X
B X
A Y
A Y
A Y
C Y
B X
B Z
A Z
A Y
A Z
A Y
A Y
B Z
A Y
B Z
C Z
B X
A Y
B Z
A Y
A X
B Y
A X
C Y
B Z
B Z
A Y
A X
B Z
C Z
B Z
A Y
A Y
A Y
A Y
A Y
B Z
A Y
A Y
B Z
A Y
A Y
A Y
A Y
B X
B Z
A Y
A Y
C Y
B Z
A Y
C Y
C Z
B Z
A Y
A Y
C Z
B Z
B Y
B X
A Y
A Y
B Z
A Y
C X
B Z
B X
B Z
B X
B Z
B Z
B Z
A Y
A Y
A Y
C Y
A Y
A Y
B Z
B X
B X
A Y
A Y
A X
A Y
A Y
A X
B X
B Y
B Z
A Y
A X
C Z
A Y
C Y
B X
A X
B Z
A Y
B Z
B Z
B X
A Y
A Y
C Z
A Y
A X
A Y
A Y
C Z
A Y
B X
A Z
B Z
B X
A Y
A X
A Y
A Z
B X
B Z
A Y
B Y
A Y
A Y
A Y
A Y
A Y
A Y
B X
C Y
A X
B Z
B X
B X
A Y
A Y
B X
A Y
C Y
A Y
A Y
B X
A Y
C X
A Y
B Z
B X
A Y
A X
C X
A Y
A Y
B Y
A Y
B Z
C Z
B X
B Y
C X
A Y
B X
A Y
B X
B Z
B Y
A Y
A Y
A Y
A Y
A Y
A Y
A Y
B X
A Y
A Y
B Z
B Z
A Y
C Y
B X
A Y
A Y
A Y
B X
A Y
B Z
A Y
B X
B Y
B X
B Y
B X
B Z
A X
B Z
C Z
B Y
A Y
A X
A Z
B Z
B Z
B Z
A Y
A Y
A Y
A Y
A Y
B Z
A Y
A Y
B Y
A Y
A Y
C Z
B Y
C Y
A Y
B Z
A Y
B Z
A Y
B X
A Z
B Z
A Y
A Y
A Y
A Y
A Y
A Y
A Y
A Y
A Y
B Z
B X
A Y
B Z
A Y
A Z
A Y
B Y
A Y
B X
B X
B Z
A Y
A Y
A Y
B Z
B Y
A Y
B X
C Z
A X
B Z
B X
A Y
A Y
A Z
B X
A X
A Y
C Y
C Y
A Y
A Y
A Y
A Y
B Z
B X
B X
A Y
B X
A Y
B X
A Y
A X
B X
B Z
A Y
B X
B X
B Z
B Y
A Y
B Z
A Y
A Y
A Y
A Y
B Y
B Y
B X
B Y
B X
B X
A Y
C X
A X
B X
A Y
B Z
A Y
A Y
B Z
B X
A Y
B Z
B X
B Z
A Y
A Y
A Y
A Y
B Y
B Z
A X
B Z
B X
A Y
A Y
C Z
A Y
B X
B Z
A Y
A Y
C X
A Y
C Y
A Z
A Y
B Y
B X
A Y
B Z
A Y
A Y
A Y
A Y
A X
B Z
B X
B Z
A Y
A Y
B X
A Y
C Z
B X
B X
A Y
A Y
B X
B Y
A Y
A Y
A Y
B Z
A X
A Y
A Y
A Y
A Y
B X
B Z
C Y
B Z
B X
A Y
B Z
A Y
B Z
A Y
C X
A Y
A Y
C Y
A Y
A Y
A Y
A Y
A Y
B X
B Y
A X
A Y
B Z
C Y
A Y
A Y
B X
A X
A X
B X
A Y
A Y
A Y
A X
C Y
B X
A Y
A Y
A Y
A Y
A Y
A Y
B Z
A Y
B Z
C Y
A Y
A Y
A Y
A Y
B Z
B Z
A X
A Y
A X
A X
A Y
A Y
B Z
B X
A Y
A Y
B X
B Y
C Z
A X
A X
A Y
B X
A Y
B X
B Z
A Y
B X
A Y
A Y
B Z
B X
B X
B X
A Y
A Y
B Z
B Z
A Y
B Y
A Y
A Y
A Y
A Y
B X
A X
B Y
B X
A Y
C X
B Z
B X
A Y
B X
B X
B X
B Y
B Y
A Y
A Z
B Z
C Y
A Y
A Y
A Z
A X
A Y
C Y
A Y
B Z
A Y
C Y
C Y
B Z
A Y
B Z
B Z
A Y
B Z
A Y
C Y
B Z
B X
B X
A Y
A Y
C Y
A Y
A Y
A Y
A X
A Y
A Y
A Y
C Z
B X
B Y
B X
A Y
A Y
C Y
A Y
A Y
A Y
B Z
B Y
A X
B Z
A Y
A Y
C Y
A Y
A Y
C Y
B X
B X
A Y
C Z
A Y
A Y
A Y
C Y
B Y
B Z
B Y
C X
A Y
B Y
C Y
B Z
A Y
B X
B X
A Y
A Y
A Y
B Y
B Y
A Y
A Y
B X
A Y
B Y
A Y
A Y
B Z
B Z
A Z
B X
B Z
B X
A Y
A Y
B Z
B Z
C Y
A Y
B Z
B Y
A Y
B X
B Z
B Z
A X
B X
A Y
A Z
B Z
A Y
B X
A Y
A Y
A Y
B X
B X
B Z
A Y
A Y
A X
C X
A Y
A X
B Z
B Z
A Y
C Y
B Z
B Z
B Y
B Z
A X
A Y
A Y
B Z
B X
A Y
C Z
A X
A Y
B Z
B X
C Y
A Y
A Y
B Y
B X
A Z
B X
A Y
A Y
B Z
C Z
B Z
B Z
A Y
A Y
A Y
B X
A Y
A X
C X
A Y
A Y
B Z
A Y
B Y
B X
A Z
A Y
A Y
A Y
C Y
B X
B Y
A Y
B Y
C Z
B X
B Z
B Z
B X
A Y
B Z
B X
A Y
A X
B Y
A Y
A Z
B X
B Z
A Y
C Z
B X
B Z
A Y
A X
A Y
B Z
B Z
A X
C Y
B X
C Z
B Y
A X
B X
C Y
A Y
B Y
B Z
A Y
A Y
A Y
A Y
B Y
B Z
B X
B X
A Y
A Z
B X
A Y
A Y
A Y
A X
B Z
C Z
C Y
B X
A Y
A Y
A Y
C X
B Z
B Z
A Y
A X
B X
A Y
B X
A X
B X
B Z
B X
B X
A Y
A Y
B X
A Y
A Y
A Y
B Z
B Y
B Z
A Y
A Y
A Y
B Z
A Y
A Y
A Y
C Y
B Y
B Z
A Y
B X
B Z
B Y
B X
A Y
A Y
A Y
A Y
C Z
A Y
A X
A Y
A Y
A Y
A Y
B Z
B Z
B Z
C Y
A Y
A Y
A Y
A Z
A Y
C Y
A Y
A Y
B Z
A Y
A Y
A Y
B X
A Y
B Y
A Y
A Y
B Z
B X
A Y
A Y
B Y
B X
A Y
B X
A Y
A Y
A Y
A Z
A Y
B X
B Y
B X
C Y
B Z
A X
A Y
A Y
A Y
B Z
B X
B X
B Z
B Y
A Y
A Z
A Y
C Z
B X
A Y
B Z
B Z
B Y
B X
A Y
C X
A Y
A Y
A Y
A Y
B Z
B Z
A Y
A Y
A Y
B Z
A Y
A Y
A Y
A Y
A Y
A Y
A Y
B X
A Y
C Y
B Z
B Z
A Y
A Y
A Y
B Y
A X
B Z
A X
B Z
B Y
A Y
B Z
B X
B X
A Y
A Y
A Y
B Z
A Y
A Y
B X
B X
A Y
B X
A Y
B X
A Y
B Z
A Y
B X
A Z
B Z
A Y
C Y
A Y
A Y
C Y
A Y
A Y
A X
A Y
C Y
A Y
A Y
B X
A Y
A Y
B X
C Y
A Y
B X
C Z
B Z
B Y
A Y
B Z
B Y
A X
A X
A Y
A Y
A Y
B X
B Z
C Y
B X
B Z
A Y
A Y
A Y
A Y
B X
B Y
C Y
A Y
A Y
A Y
B Z
B Y
A Y
B X
B Z
A Y
A Y
A Y
A Y
B Y
A X
A X
B Z
B Y
C Y
B Z
B Z
A Y
A Y
B Z
A Y
B Z
C X
A Y
A Y
B Y
A Y
B Z
A Y
B Z
B Z
A Y
A Y
C Z
C Y
A Y
A Y
C Y
A Y
C Y
A Y
B Z
A Y
B X
A X
B Z
A Y
A Y
A Y
B Z
A Z
C Y
A Y
A Y
A Y
B X
B X
A Y
A Y
A X
A Y
B Y
B X
B X
A Y
A Y
C Y
A Z
A Y
B X
B X
B Z
A Y
A Y
B Y
C Y
B X
A Y
A Y
A Y
A Y
A X
B X
A Y
A Y
B Z
A X
C Y
B X
A Y
B Z
A Y
A Y
C Y
A Y
A X
A Y
A Y
B Z
A Y
C Z
A Y
B X
B X
B Y
B Z
A Y
A Y
A Y
B Z
A Y
B Z
A Y
A X
A Z
A Y
C Z
B X
A Y
B Z
B Y
A Y
B X
B Z
B Z
B Z
A Y
A X
B Y
B X
A Y
A Y
A Y
B X
A Y
A Y
B Z
A Y
C Y
B X
A Y
A Y
C Z
B Z
A Y
B Z
B Z
B Z
A Y
B Z
B Y
A Y
A Y
C Y
A Y
B Y
A Y
B X
A Y
C Z
A Y
B X
A X
A Y
A Y
B Z
A Y
B X
B Z
B X
A Y
A Y
A Y
A Y
B Z
A Y
B Z
A Y
A Y
C Y
A Y
C Y
B X
B X
A Y
A X
B Z
B X
A Y
A Y
A Y
A Y
B Y
C Y
A X
B X
A Y
C Y
B Y
A Y
B Y
B Z
A Y
B Z
B X
A Y
B X
A Y
C Y
A Y
B X
B Z
A Y
A Y
A Y
A X
A Y
A Z
C Z
A Y
B Z
A Y
B X
B X
A Y
C Y
C Y
A Y
A Y
B Y
A Y
C Z
B Z
C Y
B X
A Y
B Z
A Y
B X
C Y
B X
A Y
A Y
B X
B Z
A Y
B Z
C Y
B X
A Y
B Z
A Y
B Z
B Z
B Z
A Y
A Y
A Y"""

assert EncryptedRockPaperScissors(example).total_score() == 15
print("Part 1:", EncryptedRockPaperScissors(puzzle).total_score())