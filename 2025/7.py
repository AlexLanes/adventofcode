from helpers import LoadPuzzleInput, Grid, Position

class Laboratories (LoadPuzzleInput):
    def __init__ (self) -> None:
        super().__init__()
        self.grid = Grid([
            list(line)
            for line in self.puzzle.splitlines()
        ])
        self.start_x = self.puzzle.index("S", 0, self.grid.size[1])

    def count_splits (self) -> int:
        splits = set[Position]()
        beams: dict[int, set[Position]] = {
            0: set(),
            1: {p := Position(1, self.start_x)}
        }
        self.grid[p] = "|"

        for y in range(2, self.grid.size[0]):
            del beams[y - 2]
            beams[y] = (current := set())

            for beam in beams[y - 1]:
                down = beam.copy().move(row=1)
                if not self.grid.in_bounds(down): continue

                match self.grid[down]:
                    case "|": continue
                    case ".": current.add(down)
                    case "^":
                        splits.add(down)
                        current.add(down.copy().move(col=-1))
                        current.add(down.copy().move(col=+1))
                    case _: raise ValueError

        return len(splits)

example = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

print("Example 1:", s := Laboratories.FromText(example).count_splits())
assert s == 21, s

print("Solution 1:", s := Laboratories().count_splits())