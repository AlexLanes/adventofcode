from typing import Generator, Literal, Self
from helpers import Grid, Position

class TransparentOrigami:

    EMPTY, DOT = " ", "."
    grid: Grid[Literal[" ", "."]] # empty or dot
    folds: list[tuple[Literal["col", "row"], int]]

    def __init__ (self, s: str) -> None:
        dots, folds = s.split("\n\n")

        self.folds = [
            ("col" if f[0][-1] == "x" else "row", int(f[1]))
            for fold in folds.split("\n")
            if (f := fold.split("="))
        ]

        max_x = max_y = 0
        positions: set[tuple[int, int]] = set()
        for dot in dots.split("\n"):
            x, y = map(int, dot.split(","))
            max_x, max_y = max(max_x, x), max(max_y, y)
            positions.add((y, x))

        row_size, col_size = max_y + 1, max_x + 1
        self.grid = Grid([
            [
                self.DOT if (row, col) in positions else self.EMPTY
                for col in range(col_size)
            ]
            for row in range(row_size)
        ])

    def positions_from_bottom (self) -> Generator[Position, None, None]:
        for row in range(self.grid.size[0] - 1, -1, -1):
            for col in range(self.grid.size[1]):
                yield Position(row, col)

    def positions_from_right (self) -> Generator[Position, None, None]:
        for row in range(self.grid.size[0]):
            for col in range(self.grid.size[1] - 1, -1, -1):
                yield Position(row, col)

    def fold_row (self, row: int) -> None:
        bottom_grid, self.grid = (
            Grid([
                self.grid.grid[row_index]
                for row_index in rows
            ])
            for rows in (
                range(row + 1, self.grid.size[0]),
                range(0, row)
            )
        )
        for top, bottom in zip(self.positions_from_bottom(), bottom_grid):
            dot = self.DOT in (bottom_grid[bottom], self.grid[top])
            self.grid[top] = self.DOT if dot else self.EMPTY

    def fold_col (self, col: int) -> None:
        right_grid = Grid([
            self.grid.grid[row][col + 1 : ]
            for row in range(self.grid.size[0])
        ])
        self.grid = Grid([
            self.grid.grid[row][ : col]
            for row in range(self.grid.size[0])
        ])
        for left, right in zip(self.positions_from_right(), right_grid):
            dot = self.DOT in (right_grid[right], self.grid[left])
            self.grid[left] = self.DOT if dot else self.EMPTY

    def fold (self, first_only=True) -> Self:
        folds = [self.folds[0]] if first_only else self.folds
        for at, rc in folds:
            func = self.fold_row if at == "row" else self.fold_col
            func(rc)
        return self

    def count_dots (self) -> int:
        return sum(
            1
            for p in self.grid
            if self.grid[p] == self.DOT
        )

example = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""
puzzle = """"""

assert TransparentOrigami(example).fold().count_dots() == 17
assert TransparentOrigami(example).fold(False).count_dots() == 16
print("First fold:", TransparentOrigami(puzzle).fold().count_dots())

t = TransparentOrigami(puzzle).fold(False)
print("All folds:", t.count_dots())
t.grid.print()