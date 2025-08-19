"""
The engineers just need the total calibration result,
which is the sum of the test values from just the equations that could possibly be true
Operators are always evaluated left-to-right, not according to precedence rules
    add (+) and multiply (*).
"""

example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
puzzle_input = """"""

class Equations:

    equations: dict[int, list[list[int]]]

    def __init__ (self, s: str) -> None:
        self.equations = {}
        for line in s.split("\n"):
            left, right = line.split(": ")
            total, values = int(left), [*map(int, right.split(" "))]

            if total not in self.equations: self.equations[total] = []
            self.equations[total].append(values)

    @staticmethod
    def is_valid (total: int, values: list[int]) -> bool:
        def recursion (current: int, waiting: tuple[int]) -> bool:
            if not waiting: return total == current
            value, *waiting = waiting
            return recursion(current + value, waiting) or recursion(current * value, waiting)

        return recursion(0, tuple(values))

    def sum_of_valids (self) -> int:
        return sum (
            total
            for total, all_values in self.equations.items()
            for values in all_values
            if self.is_valid(total, values)
        )

assert Equations(example).sum_of_valids() == 3749
# print(Equations(puzzle_input).sum_of_valids())