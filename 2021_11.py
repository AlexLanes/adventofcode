from typing import Self
from helpers import Grid, Position

class DumboOctopus:

    grid: Grid[int]
    flashes: int

    def __init__ (self, s: str) -> None:
        self.flashes = 0
        self.grid = Grid([
            list(map(int, line))
            for line in s.split("\n")
        ])

    def step_position (self, position: Position) -> None:
        val = self.grid[position]
        if val == -1: return
        if val < 9:
            self.grid[position] += 1
            return

        self.flashes += 1
        self.grid[position] = -1
        for adjacent in position.adjacents(True):
            if not self.grid.in_bounds(adjacent): continue
            self.step_position(adjacent)

    def step_n (self, n=1) -> Self:
        assert n >= 1

        for _ in range(n):
            # step each position
            for position in self.grid:
                self.step_position(position)
            # flashed current step, reset to 0
            for position in self.grid:
                if self.grid[position] == -1:
                    self.grid[position] = 0

        return self

    def step_of_simultaneously_flashes (self) -> int:
        steps = step_flashes = 0
        size = self.grid.size[0] * self.grid.size[1]

        while step_flashes != size:
            # step each position
            steps += 1
            for position in self.grid:
                self.step_position(position)
            # flashed current step, reset to 0
            step_flashes = 0
            for position in self.grid:
                if self.grid[position] == -1:
                    self.grid[position] = 0
                    step_flashes += 1

        return steps

example = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""
puzzle = """6636827465
6774248431
4227386366
7447452613
6223122545
2814388766
6615551144
4836235836
5334783256
4128344843"""

assert DumboOctopus(example).step_n(100).flashes == 1656
assert DumboOctopus(example).step_of_simultaneously_flashes() == 195
print("Part 1:", DumboOctopus(puzzle).step_n(100).flashes)
print("Part 2:", DumboOctopus(puzzle).step_of_simultaneously_flashes())