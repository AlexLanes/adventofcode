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
puzzle = """"""

assert EncryptedRockPaperScissors(example).total_score() == 15
print("Part 1:", EncryptedRockPaperScissors(puzzle).total_score())