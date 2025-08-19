from typing import Self
from helpers import Grid, Position

class GiantSquidBingo:

    numbers: list[str]
    current_number_index: int
    grids: list[Grid[str]]
    bingos: list[Grid[str]]

    def __init__ (self, s: str) -> None:
        numbers, *grids = s.split("\n\n")
        self.numbers = numbers.split(",")
        self.grids = [
            Grid([
                [num.strip() for num in line.split(" ") if num.strip()]
                for line in grid.split("\n")
            ])
            for grid in grids
        ]
        self.current_number_index = 0
        self.bingos = []

    def mark_current_number (self) -> bool:
        bingo = False
        for grid in self.grids:
            if grid in self.bingos:
                continue

            for position in grid:
                if grid[position] != self.numbers[self.current_number_index]:
                    continue

                grid[position] = "X"
                if self.check_bingo(grid, position):
                    self.bingos.append(grid)
                    bingo = True
                break

        return bingo

    def check_bingo (self, grid: Grid, position: Position) -> bool:
        checks: list[bool] = []
        row = Position(position.row, 0), { "col": +1 }
        col = Position(0, position.col), { "row": +1 }

        for position, offset in (row, col):
            valid = True
            while valid and grid.in_bounds(position):
                valid = grid[position] == "X"
                position.move(**offset)
            checks.append(valid)

        return any(checks)

    def play_to_first_win (self) -> Self:
        while not self.mark_current_number():
            self.current_number_index += 1
        return self

    def play_to_last_win (self) -> Self:
        while len(self.grids) != len(self.bingos):
            self.mark_current_number()
            self.current_number_index += 1
        self.current_number_index -= 1
        return self

    def final_score (self) -> int:
        assert self.bingos
        bingo = self.bingos[-1]
        return int(self.numbers[self.current_number_index]) * sum(
            int(bingo[position])
            for position in bingo
            if bingo[position] != "X"
        )

example = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""
puzzle = """"""

assert GiantSquidBingo(example).play_to_first_win().final_score() == 4512
assert GiantSquidBingo(example).play_to_last_win().final_score() == 1924
print("Part 1:", GiantSquidBingo(puzzle).play_to_first_win().final_score())
print("Part 2:", GiantSquidBingo(puzzle).play_to_last_win().final_score())