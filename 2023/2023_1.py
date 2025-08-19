"""
What is the sum of all of the calibration values?
The calibration value can be found by
    Combining the first digit and the last digit (in that order) to form a single two-digit number
"""

example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
puzzle_input = """"""

class CalibrationValues:

    calibrations: list[str]

    def __init__ (self, s: str) -> str:
        self.calibrations = s.split("\n")

    def value (self, calibration: str) -> int:
        nums = ["", ""]

        for char in calibration:
            if char.isdigit():
                nums[0] = char
                break
        for char in reversed(calibration):
            if char.isdigit():
                nums[1] = char
                break

        assert all(nums)
        return int("".join(nums))

    def sum_calibration_values (self) -> int:
        return sum(map(self.value, self.calibrations))

assert CalibrationValues(example).sum_calibration_values() == 142
print("Part 1:", CalibrationValues(puzzle_input).sum_calibration_values())



"""
--- Part 2 ---
Some of the digits are actually spelled out with letters:
    one, two, three, four, five, six, seven, eight, and nine
"""

from typing import Iterable

example = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

class Trie:

    type Node = dict[str, Node]
    node: Node

    def __init__ (self, words: Iterable[str]) -> None:
        self.node = {}
        for word in words: self.add_word(word)

    def add_word (self, word: str) -> None:
        node = self.node
        for char in word:
            if char not in node: node[char] = {}
            node = node[char]

    def starts_with (self, prefix: Iterable[str]) -> bool:
        node = self.node
        for char in prefix:
            if char not in node: return False
            node = node[char]
        return True

class CalibrationValuesWithLetters (CalibrationValues):

    digits = {
        text: num
        for num, text in zip(
            range(1, 10),
            "one, two, three, four, five, six, seven, eight, nine".split(", ")
        )
    }
    trie = Trie(digits)

    def value (self, calibration: str) -> int:
        nums: list[str] = []
        digit_builder = nums.copy()

        for char in calibration:
            if char.isdigit():
                nums.append(char)
                digit_builder.clear()
                continue

            digit_builder.append(char)
            if not self.trie.starts_with(digit_builder):
                digit_builder.pop(0)
            if not self.trie.starts_with(digit_builder):
                digit_builder = [char]

            if len(digit_builder) >= 3 and (digit := "".join(digit_builder)) in self.digits:
                nums.append(digit)
                digit_builder = [char]

        return int("".join(
            str(self.digits.get(num, num)) # letter to digit | num
            for num in (nums[0], nums[-1])
        ))

assert CalibrationValuesWithLetters(example).sum_calibration_values() == 281
print("Part 2:", CalibrationValuesWithLetters(puzzle_input).sum_calibration_values())