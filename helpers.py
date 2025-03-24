import typing

class Position:

    row: int
    col: int

    def __init__ (self, row: int, col: int) -> None:
        self.row, self.col = row, col

    def __iter__ (self) -> typing.Generator[int, None, None]:
        yield self.row
        yield self.col

    def __hash__ (self) -> int:
        return hash(tuple(self))

    def __eq__ (self, value: object) -> bool:
        return isinstance(value, Position) \
            and tuple(self) == tuple(value)

    def __lt__ (self, value: object) -> bool:
        return isinstance(value, Position) \
            and tuple(self) < tuple(value)

    def __le__ (self, value: object) -> bool:
        return isinstance(value, Position) \
            and tuple(self) <= tuple(value)

    def __repr__ (self) -> str:
        return f"<Position ({self.row}, {self.col})>"

    def copy (self) -> "Position":
        return Position(self.row, self.col)

    def move (self, row=0, col=0) -> typing.Self:
        self.row += row
        self.col += col
        return self

    def adjacents (self, diagonals=True) -> list["Position"]:
        (r, c), P = self, Position
        adjacents = [P(r - 1, c), P(r, c - 1), P(r, c + 1), P(r + 1, c)]
        if diagonals: adjacents.extend([
            P(r - 1, c - 1), P(r - 1, c + 1),
            P(r + 1, c - 1), P(r + 1, c + 1)
        ])
        return adjacents

class Grid [T]:

    grid: list[list[T]]
    size: tuple[int, int]

    def __init__ (self, grid: list[list[T]]) -> None:
        self.grid = grid
        self.size = (len(self.grid), len(self.grid[0]))

    def __eq__ (self, value: object) -> bool:
        return isinstance(value, Grid) \
            and self.size == value.size \
            and self.grid == value.grid

    def __getitem__ (self, position: Position) -> T:
        row, col = position
        return self.grid[row][col]

    def __setitem__ (self, position: Position, value: T) -> None:
        row, col = position
        self.grid[row][col] = value

    def __iter__ (self) -> typing.Generator[Position, None, None]:
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                yield Position(row, col)

    def print (self, file=None) -> None:
        cols_max_lengths = [
            max(
                len(str(self.grid[row][col]))
                for row in range(self.size[0])
            )
            for col in range(self.size[1])
        ]
        for row in self.grid:
            print(*(
                str(r) + " " * (cols_max_lengths[i] - len(str(r)))
                for i, r in enumerate(row)
            ), file=file)

    def in_bounds (self, position: Position) -> bool:
        return all(
            0 <= p < s
            for p, s in zip(position, self.size)
        )

def windows[T] (items: typing.Sequence[T], size=2) -> typing.Generator[tuple[T, ...], None, None]:
    assert size >= 2 and size <= len(items)
    index = 0
    while index + size <= len(items):
        yield tuple(items[i] for i in range(index, index + size))
        index += 1
