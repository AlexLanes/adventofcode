from helpers import LoadPuzzleInput, Grid

class PrintingDepartment (LoadPuzzleInput):
    def __init__ (self) -> None:
        super().__init__()
        self.grid = Grid([
            list(line)
            for line in self.puzzle.splitlines()
        ])

    def count_rolls (self) -> int:
        count = 0
        grid = self.grid

        for position in grid:
            if grid[position] != "@":
                continue

            rolls = 0
            for adj in position.adjacents(diagonals=True):
                if grid.in_bounds(adj) and grid[adj] == "@":
                    rolls += 1
                if rolls == 4: break

            if rolls < 4: count += 1

        return count

example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

print("Example 1:", example1 := PrintingDepartment.FromText(example).count_rolls())
assert example1 == 13, example1

print("Solution 1:", PrintingDepartment().count_rolls())