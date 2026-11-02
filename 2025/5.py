from helpers import LoadPuzzleInput

class Cafeteria (LoadPuzzleInput):
    def __init__ (self) -> None:
        super().__init__()

        ranges, ingredients = self.puzzle.split("\n\n")
        self.ingredients = list(map(int, ingredients.splitlines()))

        self.ranges = list[tuple[int, int]]()
        for _range in ranges.splitlines():
            l, r = _range.split("-")
            self.ranges.append((int(l), int(r)))

    def is_fresh (self, ingredient: int) -> bool:
        for l, r in self.ranges:
            if l <= ingredient <= r:
                return True
        return False

    def how_many_fresh (self) -> int:
        return sum(
            1
            for ingredient in self.ingredients
            if self.is_fresh(ingredient)
        )

example = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

print("Example 1: ", fresh := Cafeteria.FromText(example).how_many_fresh())
assert fresh == 3

print("Solution 1:", Cafeteria().how_many_fresh())