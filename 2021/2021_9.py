from collections import deque
from helpers import Grid, Position

class SmokeBasin:

    grid: Grid[int]

    def __init__ (self, s: str) -> None:
        self.grid = Grid([
            list(map(int, line))
            for line in s.split("\n")
        ])

    def low_points (self) -> list[Position]:
        return [
            position
            for position in self.grid
            if all(
                self.grid[position] < self.grid[adjacent]
                for adjacent in position.adjacents(False)
                if self.grid.in_bounds(adjacent)
            )
        ]

    def sum_risk_level_of_low_points (self) -> int:
        return sum(
            self.grid[position] + 1
            for position in self.low_points()
        )

    def basin_from_low_point (self, low: Position) -> set[Position]:
        basin: set[Position] = set()
        dq = deque([(low, self.grid[low])])

        while dq:
            position, last_val = dq.popleft()
            if position in basin or not self.grid.in_bounds(position):
                continue

            val = self.grid[position]
            if val == 9 or val < last_val: continue
            basin.add(position)

            for adjacent in position.adjacents(False):
                if adjacent == position: continue
                dq.append((adjacent, val))

        return basin

    def multiply_3_largest_basin (self) -> int:
        basins = [self.basin_from_low_point(low)
                  for low in self.low_points()]
        basins.sort(reverse=True, key=len)
        a, b, c, *_ = basins
        return len(a) * len(b) * len(c)

example = """2199943210
3987894921
9856789892
8767896789
9899965678"""
puzzle = """"""

assert SmokeBasin(example).sum_risk_level_of_low_points() == 15
assert SmokeBasin(example).multiply_3_largest_basin() == 1134
print("Part 1:", SmokeBasin(puzzle).sum_risk_level_of_low_points())
print("Part 2:", SmokeBasin(puzzle).multiply_3_largest_basin())