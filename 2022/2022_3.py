import string
from itertools import batched

class Compartment:

    left:  set[str]
    right: set[str]

    def __init__ (self, compartment: str) -> None:
        middle = len(compartment) // 2
        self.left = set(compartment[: middle])
        self.right = set(compartment[middle :])

    def __repr__ (self) -> str:
        return str(self.__dict__)

    def duplicate (self) -> str:
        duplicates = self.left.intersection(self.right)
        assert len(duplicates) == 1
        return duplicates.pop()

    def intersection (self, s: set[str]) -> set[str]:
        return self.right.union(self.left).intersection(s)

class Rucksack:

    compartments: list[Compartment]
    priorities: dict[str, int]

    def __init__ (self, s: str) -> None:
        self.compartments = [
            Compartment(compartment)
            for compartment in s.split("\n")
        ]
        self.priorities = {
            letter: priority
            for letter, priority in zip(string.ascii_letters, range(1, 53))
        }

    def sum_priorities (self) -> int:
        return sum(
            self.priorities[c.duplicate()]
            for c in self.compartments
        )

    def sum_priorities_of_group (self) -> int:
        assert len(self.compartments) % 3 == 0
        _sum = 0
        for c1, c2, c3 in batched(self.compartments, 3):
            intersection = c1.intersection(c2.intersection(c3.left | c3.right))
            assert intersection
            _sum += self.priorities[intersection.pop()]
        return _sum

example = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
puzzle_input = """"""

assert Rucksack(example).sum_priorities() == 157
assert Rucksack(example).sum_priorities_of_group() == 70
print("Part 1:", Rucksack(puzzle_input).sum_priorities())
print("Part 2:", Rucksack(puzzle_input).sum_priorities_of_group())