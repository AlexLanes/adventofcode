import itertools
from typing import Self

from helpers import Grid, Position

class RegolithReservoir:

    grid: Grid[str]
    pouring: Position
    AIR, ROCK, SAND = ".#O"

    def __init__ (self, s: str) -> None:
        rocks_ranges: list[list[Position]] = []
        min_col, max_col, max_row = 9999999, 0, 0

        for line in s.split("\n"):
            rocks = []
            for col, row in (map(int, xy.split(",")) for xy in line.split(" -> ")):
                min_col, max_col, max_row = min(min_col, col), max(max_col, col), max(max_row, row)
                rocks.append(Position(row, col))
            rocks_ranges.append(rocks)

        row_size = max_row + 1
        col_size = max_col - min_col + 3
        col_offset = min_col - 1

        self.pouring = Position(0, 500 - col_offset)
        self.grid = Grid([
            [self.AIR for _ in range(col_size)]
            for _ in range(row_size)
        ])

        pairs = (pair for rocks in rocks_ranges
                      for pair in itertools.pairwise(rocks))
        for left, right in pairs:
            for position in self.rock_range(left.copy().move(col=-col_offset),
                                            right.copy().move(col=-col_offset)):
                self.grid[position] = self.ROCK

    def rock_range (self, left: Position, right: Position):
        position = left
        row_increase, col_increase = (
            0 if a == b else 1 if a < b else -1
            for a, b in zip(left, right)
        )

        yield position
        while position != right:
            yield position.move(row_increase, col_increase)

    def drop_one_sand (self) -> bool:
        position = self.pouring.copy()
        if self.grid[position] == self.SAND:
            return False

        ok = self.grid.in_bounds
        while True:
            found, current = False, position.copy()
            for r, c in ((1, 0), (0, -1), (0, 2)):
                if ok(current.move(r, c)) and self.grid[current] == self.AIR:
                    self.grid[current], self.grid[position] = self.SAND, self.AIR
                    found, position = True, current
                    break

            if not found: break

        # left and right cols are only air
        # last row with sand flows into abyss
        if position.row == self.grid.size[0] - 1:
            self.grid[position] = self.AIR
            return False

        return True

    def count_sand_drops (self) -> int:
        drops = 0
        while self.drop_one_sand():
            drops += 1
        return drops

    def add_floor (self) -> Self:
        self.grid.grid.append([self.AIR for _ in range(self.grid.size[1])])
        self.grid.grid.append([self.ROCK for _ in range(self.grid.size[1])])
        return self

example = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
puzzle = """"""

assert RegolithReservoir(example).count_sand_drops() == 24
print("Part 1:", RegolithReservoir(puzzle).count_sand_drops())

print(RegolithReservoir(example).add_floor())