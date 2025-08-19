from helpers import Grid, Position

class HydrothermalVenture:

    ranges: list[tuple[Position, Position]]
    grid: Grid[int]

    def __init__ (self, s: str, vertical=False) -> None:
        self.ranges = []
        for line in s.split("\n"):
            left, right = sorted(
                Position(*map(int, reversed(part.split(","))))
                for part in line.split(" -> ")
            )
            r = (left, right)
            if not vertical and not any(a == b for a, b in zip(*r)):
                continue
            self.ranges.append(r)

        self.create_grid()
        self.add_vents()

    def create_grid (self) -> None:
        row_size = max(p.row for r in self.ranges for p in r) + 1
        col_size = max(p.col for r in self.ranges for p in r) + 1
        self.grid = Grid([
            [0 for _ in range(col_size)]
            for _ in range(row_size)
        ])

    def add_vents (self) -> None:
        for left, right in self.ranges:
            position, increments = left.copy(), {
                "row": 0 if (r := right.row - left.row) == 0 else r // abs(r), # -1 0 1
                "col": 0 if (c := right.col - left.col) == 0 else c // abs(c), # -1 0 1
            }
            while position <= right:
                self.grid[position] += 1
                position.move(**increments)

    def count_overlaps (self) -> int:
        return sum(
            1
            for position in self.grid
            if self.grid[position] > 1
        )

example = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""
puzzle = """"""

assert HydrothermalVenture(example).count_overlaps() == 5
assert HydrothermalVenture(example, True).count_overlaps() == 12
print("Part 1:", HydrothermalVenture(puzzle).count_overlaps())
print("Part 2:", HydrothermalVenture(puzzle, True).count_overlaps())