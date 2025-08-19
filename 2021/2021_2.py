from helpers import Position

class Dive:

    moves: list[tuple[str, int]]

    def __init__ (self, s: str) -> None:
        self.moves = []
        for line in s.split("\n"):
            left, right = line.split(" ")
            self.moves.append((left, int(right)))

    def move_and_mult (self) -> int:
        position = Position(0, 0)
        for move, x in self.moves:
            if move == "forward": position.move(col=x)
            elif move == "down": position.move(row=x)
            else: position.move(row=-x)
        return position.row * position.col

    def move_and_mult_with_aim (self) -> int:
        aim, position = 0, Position(0, 0)
        for move, x in self.moves:
            if move == "up": aim -= x
            elif move == "down": aim += x
            else: position.move(x * aim, x)
        return position.row * position.col

example = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""
puzzle = """"""

assert Dive(example).move_and_mult() == 150
assert Dive(example).move_and_mult_with_aim() == 900
print("Part 1:", Dive(puzzle).move_and_mult())
print("Part 2:", Dive(puzzle).move_and_mult_with_aim())