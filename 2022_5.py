import re as regex

class Stack [T]:

    stack: list[T]

    def __init__ (self) -> None:
        self.stack = []

    def __str__ (self) -> str:
        return str(self.stack)

    def push (self, *n: T) -> None:
        self.stack.extend(n)

    def pop (self) -> T:
        return self.stack.pop(-1)

    def peek (self) -> T:
        return self.stack[-1]

class Move:
    def __init__ (self, m: str) -> None:
        self.crates, self.origin, self.to = map(int, regex.findall(r"\d+", m))

    def __str__ (self) -> str:
        return str(self.__dict__)

class SupplyStacks:

    crates: dict[int, Stack[str]]
    moves: list[Move]

    def __init__ (self, s: str) -> None:
        start, moves = s.split("\n\n", 1)

        self.crates = {}
        self.moves = list(map(Move, moves.split("\n")))

        crates = start.split("\n")
        crates_index = crates.pop(-1)
        for match in regex.finditer(r"\d", crates_index):
            index, stack = match.start(), Stack()
            for crate in reversed(crates):
                if (char := crate[index]) != " ":
                    stack.push(char)
            self.crates[int(match.group())] = stack

    def rearrange (self) -> str:
        for move in self.moves:
            origin, to = self.crates[move.origin], self.crates[move.to]
            for _ in range(move.crates):
                to.push(origin.pop())

        return "".join(
            s.peek()
            for s in self.crates.values()
        )

    def rearrange_multiple (self) -> str:
        for move in self.moves:
            origin, to = self.crates[move.origin], self.crates[move.to]
            crates = reversed([ origin.pop() for _ in range(move.crates) ])
            to.push(*crates)

        return "".join(
            s.peek()
            for s in self.crates.values()
        )

example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
puzzle = """    [M]             [Z]     [V]    
    [Z]     [P]     [L]     [Z] [J]
[S] [D]     [W]     [W]     [H] [Q]
[P] [V] [N] [D]     [P]     [C] [V]
[H] [B] [J] [V] [B] [M]     [N] [P]
[V] [F] [L] [Z] [C] [S] [P] [S] [G]
[F] [J] [M] [G] [R] [R] [H] [R] [L]
[G] [G] [G] [N] [V] [V] [T] [Q] [F]
 1   2   3   4   5   6   7   8   9 

move 6 from 9 to 3
move 2 from 2 to 1
move 1 from 8 to 2
move 3 from 7 to 2
move 7 from 6 to 9
move 1 from 9 to 5
move 3 from 5 to 7
move 6 from 8 to 6
move 1 from 7 to 8
move 6 from 6 to 5
move 4 from 5 to 8
move 9 from 2 to 9
move 1 from 2 to 3
move 3 from 1 to 3
move 3 from 5 to 1
move 10 from 3 to 5
move 4 from 4 to 6
move 2 from 7 to 6
move 2 from 6 to 9
move 6 from 8 to 6
move 1 from 4 to 3
move 1 from 4 to 5
move 1 from 4 to 1
move 2 from 3 to 1
move 1 from 3 to 7
move 8 from 1 to 9
move 1 from 1 to 2
move 1 from 2 to 7
move 6 from 6 to 3
move 7 from 3 to 5
move 14 from 5 to 6
move 2 from 1 to 3
move 5 from 5 to 8
move 5 from 8 to 1
move 2 from 7 to 1
move 5 from 6 to 9
move 8 from 9 to 3
move 13 from 9 to 3
move 7 from 1 to 4
move 6 from 4 to 1
move 22 from 3 to 1
move 1 from 9 to 3
move 2 from 6 to 1
move 1 from 3 to 4
move 7 from 9 to 8
move 2 from 1 to 7
move 2 from 3 to 2
move 2 from 6 to 9
move 2 from 7 to 8
move 1 from 3 to 6
move 9 from 8 to 6
move 1 from 2 to 4
move 8 from 1 to 2
move 1 from 9 to 4
move 3 from 4 to 1
move 1 from 4 to 6
move 10 from 6 to 5
move 5 from 2 to 9
move 6 from 9 to 3
move 2 from 5 to 3
move 2 from 9 to 7
move 7 from 5 to 8
move 5 from 6 to 2
move 3 from 3 to 7
move 3 from 3 to 5
move 4 from 5 to 8
move 1 from 3 to 5
move 6 from 6 to 8
move 1 from 5 to 7
move 9 from 8 to 9
move 1 from 3 to 1
move 7 from 2 to 7
move 9 from 7 to 6
move 2 from 2 to 3
move 7 from 9 to 3
move 9 from 6 to 8
move 7 from 3 to 4
move 2 from 7 to 6
move 4 from 4 to 5
move 3 from 5 to 6
move 2 from 7 to 4
move 5 from 4 to 7
move 13 from 8 to 4
move 2 from 9 to 4
move 2 from 8 to 7
move 6 from 7 to 5
move 6 from 4 to 2
move 1 from 7 to 5
move 3 from 2 to 7
move 1 from 7 to 8
move 3 from 2 to 4
move 2 from 3 to 9
move 2 from 7 to 2
move 6 from 5 to 4
move 3 from 6 to 2
move 2 from 6 to 9
move 5 from 2 to 9
move 12 from 4 to 8
move 3 from 9 to 2
move 12 from 1 to 5
move 4 from 4 to 6
move 12 from 8 to 9
move 2 from 6 to 5
move 1 from 4 to 8
move 1 from 4 to 1
move 3 from 2 to 1
move 2 from 6 to 7
move 1 from 5 to 9
move 2 from 1 to 4
move 10 from 5 to 1
move 2 from 7 to 3
move 18 from 9 to 7
move 8 from 7 to 2
move 1 from 9 to 6
move 1 from 6 to 7
move 10 from 7 to 9
move 1 from 4 to 2
move 19 from 1 to 5
move 8 from 5 to 9
move 3 from 8 to 4
move 2 from 5 to 2
move 2 from 3 to 6
move 10 from 5 to 2
move 4 from 1 to 2
move 2 from 9 to 2
move 1 from 1 to 6
move 2 from 5 to 6
move 1 from 8 to 7
move 1 from 5 to 8
move 1 from 5 to 6
move 18 from 2 to 5
move 5 from 2 to 1
move 6 from 5 to 8
move 1 from 8 to 9
move 2 from 2 to 4
move 1 from 2 to 6
move 2 from 7 to 6
move 1 from 4 to 1
move 4 from 8 to 5
move 1 from 2 to 9
move 2 from 8 to 3
move 1 from 3 to 6
move 1 from 4 to 8
move 1 from 8 to 9
move 10 from 5 to 7
move 5 from 5 to 1
move 2 from 4 to 1
move 3 from 7 to 6
move 12 from 1 to 4
move 8 from 9 to 5
move 6 from 7 to 4
move 1 from 7 to 9
move 4 from 4 to 3
move 1 from 1 to 7
move 3 from 9 to 5
move 2 from 3 to 1
move 1 from 7 to 6
move 8 from 4 to 7
move 1 from 7 to 6
move 7 from 6 to 4
move 2 from 1 to 3
move 1 from 7 to 1
move 1 from 3 to 7
move 1 from 1 to 6
move 4 from 9 to 3
move 5 from 4 to 6
move 12 from 6 to 2
move 3 from 9 to 4
move 8 from 2 to 6
move 2 from 9 to 6
move 8 from 5 to 6
move 4 from 5 to 8
move 14 from 6 to 3
move 11 from 4 to 9
move 2 from 2 to 7
move 8 from 3 to 9
move 11 from 3 to 6
move 14 from 9 to 1
move 7 from 1 to 3
move 2 from 9 to 5
move 2 from 2 to 8
move 6 from 7 to 5
move 1 from 9 to 8
move 13 from 6 to 3
move 4 from 6 to 8
move 3 from 1 to 6
move 5 from 5 to 8
move 7 from 8 to 7
move 2 from 1 to 8
move 1 from 4 to 1
move 4 from 8 to 9
move 8 from 7 to 5
move 1 from 8 to 1
move 4 from 9 to 3
move 1 from 4 to 5
move 5 from 5 to 2
move 1 from 8 to 9
move 1 from 8 to 6
move 2 from 6 to 2
move 4 from 8 to 6
move 4 from 1 to 8
move 4 from 8 to 5
move 1 from 9 to 8
move 1 from 2 to 3
move 4 from 6 to 1
move 1 from 8 to 2
move 3 from 5 to 4
move 4 from 2 to 5
move 1 from 7 to 9
move 1 from 2 to 6
move 3 from 1 to 8
move 2 from 4 to 5
move 2 from 6 to 1
move 3 from 8 to 9
move 4 from 9 to 2
move 1 from 7 to 1
move 1 from 6 to 7
move 4 from 1 to 6
move 1 from 7 to 4
move 6 from 2 to 8
move 2 from 4 to 8
move 1 from 9 to 5
move 3 from 6 to 2
move 1 from 6 to 4
move 7 from 3 to 5
move 2 from 8 to 1
move 3 from 2 to 8
move 6 from 8 to 5
move 17 from 5 to 3
move 2 from 1 to 6
move 3 from 8 to 3
move 1 from 9 to 5
move 11 from 5 to 2
move 40 from 3 to 5
move 11 from 2 to 7
move 4 from 7 to 8
move 1 from 8 to 9
move 1 from 3 to 5
move 1 from 4 to 8
move 19 from 5 to 8
move 7 from 7 to 8
move 16 from 5 to 2
move 6 from 5 to 8
move 1 from 5 to 8
move 1 from 9 to 4
move 1 from 6 to 1
move 1 from 4 to 7
move 1 from 6 to 9
move 1 from 1 to 7
move 1 from 7 to 3
move 1 from 7 to 2
move 1 from 9 to 8
move 1 from 3 to 4
move 1 from 4 to 6
move 14 from 2 to 9
move 24 from 8 to 4
move 8 from 8 to 3
move 1 from 6 to 3
move 16 from 4 to 1
move 3 from 8 to 4
move 3 from 3 to 8
move 4 from 3 to 4
move 1 from 3 to 9
move 13 from 9 to 4
move 16 from 1 to 8
move 8 from 8 to 1
move 3 from 1 to 7
move 1 from 8 to 6
move 1 from 3 to 8
move 10 from 8 to 5
move 5 from 5 to 2
move 3 from 8 to 9
move 1 from 8 to 9
move 1 from 4 to 5
move 5 from 2 to 6
move 3 from 5 to 2
move 1 from 6 to 1
move 5 from 1 to 5
move 1 from 1 to 5
move 2 from 7 to 3
move 2 from 3 to 2
move 1 from 5 to 7
move 7 from 5 to 3
move 5 from 9 to 5
move 2 from 7 to 9
move 4 from 5 to 6
move 2 from 9 to 8
move 2 from 2 to 4
move 5 from 3 to 5
move 1 from 3 to 2
move 7 from 4 to 9
move 1 from 8 to 1
move 1 from 2 to 1
move 9 from 4 to 6
move 2 from 1 to 8
move 1 from 3 to 9
move 2 from 8 to 6
move 13 from 4 to 6
move 1 from 8 to 7
move 2 from 9 to 6
move 3 from 5 to 7
move 3 from 2 to 5
move 3 from 2 to 6
move 5 from 6 to 2
move 4 from 2 to 5
move 4 from 5 to 7
move 5 from 5 to 7
move 7 from 9 to 6
move 6 from 7 to 2
move 22 from 6 to 5
move 10 from 5 to 8
move 7 from 5 to 4
move 8 from 8 to 5
move 18 from 6 to 2
move 5 from 7 to 5
move 1 from 8 to 2
move 6 from 5 to 1
move 7 from 4 to 2
move 4 from 1 to 5
move 1 from 7 to 9
move 1 from 8 to 6
move 1 from 7 to 8
move 10 from 5 to 9
move 12 from 2 to 1
move 8 from 5 to 2
move 19 from 2 to 9
move 1 from 6 to 8
move 13 from 9 to 3
move 8 from 1 to 2
move 5 from 1 to 3
move 10 from 2 to 1
move 7 from 2 to 5
move 3 from 5 to 7
move 4 from 1 to 3
move 1 from 2 to 3
move 3 from 1 to 2
move 1 from 8 to 6
move 2 from 7 to 5
move 4 from 1 to 3
move 6 from 5 to 4
move 2 from 2 to 1
move 1 from 2 to 9
move 6 from 4 to 5
move 5 from 5 to 9
move 1 from 6 to 8
move 1 from 5 to 1
move 6 from 9 to 2
move 5 from 2 to 4
move 3 from 1 to 6
move 2 from 4 to 7
move 22 from 3 to 9
move 1 from 8 to 4
move 2 from 4 to 3
move 2 from 6 to 1
move 2 from 1 to 5
move 1 from 6 to 7
move 1 from 7 to 4
move 6 from 3 to 7
move 1 from 2 to 4
move 8 from 7 to 3
move 1 from 4 to 5
move 1 from 7 to 9
move 5 from 3 to 6
move 1 from 8 to 4
move 4 from 3 to 2
move 32 from 9 to 3
move 3 from 6 to 7
move 5 from 9 to 3
move 1 from 9 to 7
move 2 from 9 to 2
move 2 from 4 to 3
move 2 from 5 to 4
move 5 from 3 to 2
move 3 from 7 to 8
move 1 from 7 to 2
move 1 from 8 to 5
move 1 from 3 to 4
move 5 from 4 to 5
move 4 from 5 to 2
move 3 from 5 to 7
move 1 from 7 to 5
move 1 from 6 to 5
move 2 from 8 to 5
move 15 from 2 to 4
move 3 from 5 to 6
move 4 from 6 to 5
move 2 from 5 to 2
move 1 from 2 to 4
move 25 from 3 to 9
move 2 from 5 to 2
move 11 from 9 to 2
move 13 from 2 to 1
move 4 from 4 to 7
move 12 from 9 to 8
move 6 from 7 to 8
move 7 from 4 to 7
move 7 from 7 to 8
move 1 from 5 to 1
move 5 from 4 to 3
move 2 from 2 to 1
move 2 from 9 to 5
move 7 from 1 to 7
move 1 from 1 to 4
move 12 from 3 to 2
move 1 from 3 to 9
move 1 from 1 to 3
move 1 from 9 to 1
move 7 from 7 to 2
move 1 from 4 to 7
move 2 from 8 to 7
move 7 from 1 to 2
move 1 from 3 to 4
move 26 from 2 to 1
move 4 from 8 to 1
move 3 from 1 to 6
move 1 from 6 to 3
move 1 from 6 to 9
move 1 from 3 to 8
move 20 from 1 to 3
move 1 from 9 to 7
move 4 from 7 to 1
move 1 from 5 to 3
move 4 from 3 to 5
move 1 from 6 to 2
move 6 from 3 to 2
move 8 from 1 to 4
move 1 from 1 to 5
move 3 from 1 to 4
move 7 from 2 to 4
move 10 from 3 to 8
move 4 from 4 to 3
move 12 from 4 to 7
move 3 from 3 to 1
move 2 from 4 to 3
move 2 from 8 to 1
move 6 from 8 to 9
move 5 from 9 to 6
move 1 from 9 to 3
move 3 from 8 to 7
move 10 from 8 to 5
move 4 from 8 to 7
move 9 from 7 to 9
move 4 from 8 to 4
move 2 from 4 to 3
move 3 from 1 to 7
move 11 from 7 to 4
move 6 from 4 to 8
move 1 from 7 to 3
move 4 from 5 to 1
move 5 from 3 to 6
move 5 from 9 to 4
move 1 from 9 to 8
move 10 from 4 to 8
move 5 from 1 to 2
move 1 from 7 to 6
move 9 from 6 to 3
move 7 from 8 to 7
move 3 from 4 to 1
move 2 from 2 to 1
move 9 from 8 to 3
move 10 from 5 to 8
move 18 from 3 to 9
move 1 from 7 to 8
move 1 from 5 to 3
move 4 from 8 to 3
move 2 from 6 to 3
move 6 from 7 to 2
move 1 from 5 to 3
move 1 from 1 to 9
move 10 from 3 to 9
move 4 from 1 to 8
move 13 from 8 to 1
move 3 from 1 to 8
move 3 from 2 to 4
move 5 from 2 to 6
move 5 from 6 to 4
move 28 from 9 to 2
move 2 from 9 to 5
move 2 from 5 to 2
move 1 from 3 to 7
move 2 from 1 to 4
move 3 from 8 to 3
move 1 from 9 to 4
move 3 from 4 to 6
move 2 from 3 to 7
move 8 from 1 to 5
move 3 from 7 to 6
move 14 from 2 to 8
move 1 from 9 to 1
move 6 from 5 to 6
move 4 from 2 to 5
move 9 from 8 to 2
move 4 from 8 to 4
move 7 from 2 to 4
move 12 from 4 to 3
move 5 from 4 to 7
move 5 from 7 to 4
move 1 from 8 to 7
move 1 from 4 to 5
move 2 from 5 to 4
move 1 from 5 to 8
move 1 from 5 to 9"""

assert SupplyStacks(example).rearrange() == "CMZ"
print("Part 1:", SupplyStacks(puzzle).rearrange())
assert SupplyStacks(example).rearrange_multiple() == "MCD"
print("Part 2:", SupplyStacks(puzzle).rearrange_multiple())