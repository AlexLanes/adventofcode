import bisect

class Calories:

    ordered_calories: list[int]

    def __init__ (self, s: str) -> None:
        self.ordered_calories = []
        for calories in s.split("\n\n"):
            c = sum(map(int, calories.split("\n")))
            bisect.insort(self.ordered_calories, c)

    def max_calories (self) -> int:
        return self.ordered_calories[-1]

    def sum_top_3 (self) -> int:
        return sum(
            self.ordered_calories[i]
            for i in (-1, -2, -3)
        )

example = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""
puzzle_input = """"""

assert Calories(example).max_calories() == 24000
assert Calories(example).sum_top_3() == 45000
print("Part 1:", Calories(puzzle_input).max_calories())
print("Part 2:", Calories(puzzle_input).sum_top_3())