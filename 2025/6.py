import operator
from functools import reduce

from helpers import LoadPuzzleInput

class TrashCompactor (LoadPuzzleInput):
    def __init__ (self) -> None:
        super().__init__()

        lines = self.puzzle.splitlines()
        self.operations = list(lines.pop().replace(" ", ""))
        self.lines = [
            [int(part.strip()) for part in line.split() if part.strip()]
            for line in lines
        ]

        length = len(self.operations)
        assert all(len(line) == length for line in self.lines)

    def get_veritical_line (self, index: int) -> list[int]:
        return [line[index] for line in self.lines]

    def add_problems_answers (self) -> int:
        return sum(
            reduce(
                lambda a, b: operator.add(a, b)
                             if op == "+"
                             else operator.mul(a, b),
                self.get_veritical_line(index)
            )
            for index, op in enumerate(self.operations)
        )

example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

print("Example 1:", x := TrashCompactor.FromText(example).add_problems_answers())
assert x == 4277556, x

print("Solution 1:", TrashCompactor().add_problems_answers())