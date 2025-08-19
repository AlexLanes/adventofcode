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
puzzle = """"""

assert SupplyStacks(example).rearrange() == "CMZ"
print("Part 1:", SupplyStacks(puzzle).rearrange())
assert SupplyStacks(example).rearrange_multiple() == "MCD"
print("Part 2:", SupplyStacks(puzzle).rearrange_multiple())