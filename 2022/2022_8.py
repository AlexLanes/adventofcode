class Position:

    row: int
    col: int

    def __init__ (self, row: int, col: int) -> None:
        self.row, self.col = row, col

    def __iter__ (self):
        yield self.row
        yield self.col

    def __hash__ (self) -> int:
        return hash(tuple(self))

    def __eq__ (self, value: object) -> bool:
        return hash(self) == hash(value)

    def __repr__ (self) -> str:
        return f"<Position ({self.row}, {self.col})>"

    def copy (self) -> "Position":
        return Position(self.row, self.col)

    def move (self, row=0, col=0) -> "Position":
        self.row += row
        self.col += col
        return self

    def adjacents (self) -> list["Position"]:
        r, c = self
        P = Position
        return [
            P(r - 1, c - 1), P(r - 1, c), P(r - 1, c + 1),
            P(r,     c - 1),              P(r,     c + 1),
            P(r + 1, c - 1), P(r + 1, c), P(r + 1, c + 1),
        ]

class Grid:

    grid: list[str]
    size: tuple[int, int]

    ROW_COL_MOVEMENTS = (
        (-1, 0), # up
        (+1, 0), # down
        (0, -1), # left
        (0, +1), # right
    )

    def __init__ (self, s: str) -> None:
        self.grid = s.split("\n")
        self.size = (len(self.grid), len(self.grid[0]))

    def __getitem__ (self, position: Position) -> str:
        row, col = position
        return self.grid[row][col]

    def __iter__ (self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                yield Position(row, col)

    def print (self) -> None:
        for row in self.grid:
            print(*row)

    def in_bounds (self, position: Position) -> bool:
        return all(
            0 <= p < s
            for p, s in zip(position, self.size)
        )

    def is_tree_visible (self, position: Position) -> bool:
        edge = 0 in position or any(p == s - 1 for p, s in zip(position, self.size))
        if edge: return True

        tree = self[position]
        for r, c in self.ROW_COL_MOVEMENTS:

            pos, same_or_bigger = position.copy(), False
            while not same_or_bigger and self.in_bounds(pos.move(r, c)):
                same_or_bigger = self[pos] >= tree

            if not same_or_bigger: return True

        return False

    def count_visible (self) -> int:
        return sum(
            1
            for position in self
            if self.is_tree_visible(position)
        )

    def scenic_score (self, position: Position) -> int:
        edge = 0 in position or any(p == s - 1 for p, s in zip(position, self.size))
        if edge: return 0

        score, tree = 1, self[position]
        for r, c in self.ROW_COL_MOVEMENTS:

            lower, pos = 1, position.copy()
            while self.in_bounds(pos.move(r, c)):
                if self[pos] >= tree: break
                lower += 1

            score *= lower if self.in_bounds(pos) else lower - 1

        return score

    def max_scenic_score (self) -> int:
        return max(
            self.scenic_score(position)
            for position in self
        )

example = """30373
25512
65332
33549
35390"""
puzzle = """"""

assert Grid(example).count_visible() == 21
print("Part 1:", Grid(puzzle).count_visible())

assert Grid(example).max_scenic_score() == 8
print("Part 2:", Grid(puzzle).max_scenic_score())