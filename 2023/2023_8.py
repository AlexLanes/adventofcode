import itertools

class LabeledNodes:

    # instructions: itertools.cycle[int] # 0 Left | 1 Right
    elements: dict[str, tuple[str, str]]
    END = "ZZZ"
    START = "AAA"

    def __init__ (self, s: str) -> None:
        i, e = s.split("\n\n", 1)
        self.instructions = itertools.cycle([0 if char == "L" else 1 for char in i])
        self.elements = {}
        for line in e.split("\n"):
            element, elements = line.split(" = ")
            self.elements[element] = tuple(elements.strip("()").split(", "))

    def count_steps (self) -> int:
        steps, element = 0, self.START
        while element != self.END:
            instruction = next(self.instructions)
            element = self.elements[element][instruction]
            steps += 1
        return steps

"""
Starting at AAA, how many steps are required to reach ZZZ ?
You need to look up the next element based on the next left/right instruction in your input
Repeat the whole sequence of instructions as necessary
"""

example = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""
puzzle_input = """"""

assert LabeledNodes(example).count_steps() == 6
print("Part 1:", LabeledNodes(puzzle_input).count_steps())