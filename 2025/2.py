from collections import Counter

from helpers import LoadPuzzleInput

class CustomCounter:
    def __init__ (self, s: str) -> None:
        self._max = ""
        self._counter = Counter(s)

    def subtract (self, char: str) -> None:
        counter = self._counter
        counter.subtract(char)

        if counter[char] >= 1: return

        counter.pop(char)
        if char == self._max:
            self._max = ""

    def max (self) -> str:
        if m := self._max:
            return m
        m = max(self._counter)
        self._max = m
        return m

class Jolks (LoadPuzzleInput):

    banks: list[str]

    def __init__ (self) -> None:
        super().__init__()
        self.banks = self.puzzle.splitlines()

    def largest_joltage (self, bank: str) -> int:
        largest = ""
        counter = CustomCounter(bank)

        for index in range(0, len(bank) - 1):
            battery = bank[index]
            counter.subtract(battery)
            joltage = battery + counter.max()
            if joltage > largest:
                largest = joltage

        return int(largest)

    def sum_of_largest_banks (self) -> int:
        return sum(self.largest_joltage(bank)
                   for bank in self.banks)

example = """987654321111111
811111111111119
234234234234278
818181911112111"""

print("Example 1:", example1 := Jolks.FromText(example).sum_of_largest_banks())
assert example1 == 357

print("Solution 1:", Jolks().sum_of_largest_banks())