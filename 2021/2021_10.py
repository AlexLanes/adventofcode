from functools import reduce
from typing import Literal

class SyntaxScoring:

    lines: list[str]

    OPEN = "([{<"
    CLOSE_TO_OPEN = { c: o for o, c in zip(OPEN, ")]}>") }
    SCORES_ILLEGAL = { c: s for c, s in zip(CLOSE_TO_OPEN, (3, 57, 1197, 25137)) }
    SCORES_INCOMPLETE = { c: s for c, s in zip(OPEN, (1, 2, 3, 4)) }

    def __init__ (self, s: str) -> None:
        self.lines = s.split("\n")

    def first_corrupted_char (self, line: str) -> Literal["", ")", "]", "}", ">"]:
        opened_queue: list[str] = []
        for char in line:
            # open new
            if char in self.OPEN:
                opened_queue.append(char)
            # close opened
            elif self.CLOSE_TO_OPEN[char] == opened_queue[-1]:
                opened_queue.pop(-1)
            # invalid found
            else: return char # type: ignore

        return ""

    def sum_corrupted_score (self) -> int:
        return sum(
            self.SCORES_ILLEGAL.get(self.first_corrupted_char(line), 0)
            for line in self.lines
        )

    def incomplete_score (self, line: str) -> int:
        opened_queue: list[str] = []
        for char in line:
            # open new
            if char in self.OPEN:
                opened_queue.append(char)
            # close opened
            elif self.CLOSE_TO_OPEN[char] == opened_queue[-1]:
                opened_queue.pop(-1)
            # corrupted
            else: raise Exception("Corrupted line")

        return reduce(
            lambda score, opened: score * 5 + self.SCORES_INCOMPLETE[opened],
            reversed(opened_queue),
            0
        )

    def middle_of_sorted_incomplete_scores (self) -> int:
        scores = sorted(self.incomplete_score(line)
                        for line in self.lines
                        if not self.first_corrupted_char(line))
        return scores[len(scores) // 2]

example = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""
puzzle = """"""

assert SyntaxScoring(example).sum_corrupted_score() == 26397
assert SyntaxScoring(example).middle_of_sorted_incomplete_scores() == 288957
print("Part 1:", SyntaxScoring(puzzle).sum_corrupted_score())
print("Part 2:", SyntaxScoring(puzzle).middle_of_sorted_incomplete_scores())