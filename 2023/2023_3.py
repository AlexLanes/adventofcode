"""
What is the sum of all of the part numbers in the engine schematic?
Part Number:
 - Any number adjacent to a symbol, even diagonally
 - Periods (.) do not count as a symbol.
"""

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

    grid: list[list[str]]
    size: tuple[int, int]
    NOT_SYMBOLS = ".0123456789"

    def __init__ (self, s: str) -> None:
        self.grid = [
            [*line]
            for line in map(lambda char: char.strip().upper(),
                            s.split("\n"))
            if line
        ]
        self.size = (len(self.grid), len(self.grid[0]))

    def __getitem__ (self, position: Position) -> str:
        row, col = position
        return self.grid[row][col]

    def print (self) -> None:
        for row in self.grid:
            print(*row)

    def valid_position (self, position: Position) -> bool:
        return all(
            0 <= p < s
            for p, s in zip(position, self.size)
        )

    def find_horizontal_numbers_start_positions (self) -> list[Position]:
        positions = []
        for row in range(self.size[0]):
            last_was_number = False

            for col in range(self.size[1]):
                position = Position(row, col)
                char = self[position]

                if not char.isdigit():
                    last_was_number = False
                    continue
                if not last_was_number:
                    positions.append(position)
                last_was_number = True

        return positions

    def part_number (self, position: Position) -> tuple[bool, int, Position]:
        assert self[position].isdigit()

        # move to start position
        start_position = position.copy().move(col=-1)
        while self.valid_position(start_position) and self[start_position].isdigit():
            start_position.col -= 1
        start_position.move(col=1)

        # check all digits of number
        digits: list[str] = []
        is_part_number = False
        adjacents = position.adjacents()
        position = start_position.copy()

        while self.valid_position(position) and (char := self[position]).isdigit():
            digits.append(char)
            is_part_number = is_part_number or any(
                self[adjacent] not in self.NOT_SYMBOLS
                for adjacent in adjacents
                if self.valid_position(adjacent)
            )

            # move right
            position.col += 1
            for p in adjacents: p.col += 1

        return is_part_number, int("".join(digits)), start_position

    def sum_of_part_numbers (self) -> int:
        return sum(
            part_number[1]
            for position in self.find_horizontal_numbers_start_positions()
            if (part_number := self.part_number(position))[0]
        )

    def sum_of_gear_ratios (self) -> int:
        positions: list[Position] = []
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                if self[position := Position(row, col)] == "*":
                    positions.append(position)

        gear_ratios: list[int] = []
        for position in positions:
            adjacents = {
                self.part_number(adjacent)
                for adjacent in position.adjacents()
                if self[adjacent].isdigit()
            }
            if len(adjacents) != 2: continue
            a, b = (num for _, num, _ in adjacents)
            gear_ratios.append(a * b)

        return sum(gear_ratios)

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
puzzle_input = """"""

assert Grid(example).sum_of_part_numbers() == 4361
print("Part 1:", Grid(puzzle_input).sum_of_part_numbers())



"""
What is the sum of all of the gear ratios in your engine schematic?
A gear is any * symbol that is adjacent to exactly two part numbers.
Its gear ratio is the result of multiplying those two numbers together.
"""

example = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
assert Grid(example).sum_of_gear_ratios() == 467835
print("Part 2:", Grid(puzzle_input).sum_of_gear_ratios())