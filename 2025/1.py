from typing import Iterable

from helpers import LoadPuzzleInput

class SecretEntrance (LoadPuzzleInput):
    """[L/R][1..any]
    0 to 99, rotates"""

    moves: Iterable[int]
    START_POSITION = 50

    def __init__ (self) -> None:
        super().__init__()
        self.moves = (
            int(line[1:])
            if line[0] == "R" else
            -int(line[1:])
            for line in self.puzzle.splitlines()
        )

    def stops_at_0 (self) -> int:
        stops_at_0 = 0
        position = self.START_POSITION

        for move in self.moves:
            partial = abs(move) % 100

            position += partial if move >= 0 else -partial
            if position < 0: position = 100 + position
            elif position > 99: position = position - 100

            if position == 0: stops_at_0 += 1

        return stops_at_0

    def clicks_at_0 (self) -> int:
        cliks_at_0 = 0
        position = self.START_POSITION

        for move in self.moves:
            full, partial = divmod(abs(move), 100)
            cliks_at_0 += full

            last = position
            position += partial if move >= 0 else -partial

            if position == 0: cliks_at_0 += 1
            elif position < 0:
                cliks_at_0 += 1 if last != 0 else 0
                position = 100 + position
            elif position > 99:
                cliks_at_0 += 1
                position = position - 100

        return cliks_at_0

example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

print("Example 1:", stops := SecretEntrance.FromText(example).stops_at_0())
print("Example 2:", clicks := SecretEntrance.FromText(example).clicks_at_0())
assert stops == 3 and clicks == 6, (stops, clicks)

print("Solution 1:", SecretEntrance().stops_at_0())
print("Solution 2:", SecretEntrance().clicks_at_0())