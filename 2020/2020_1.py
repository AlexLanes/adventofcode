class ReportRepair:

    numbers: set[int]
    GOAL = 2020

    def __init__ (self, s: str) -> None:
        self.numbers = set(int(n) for n in s.split())

    def part_1 (self) -> int:
        for number in self.numbers:
            x = self.GOAL - number
            if x in self.numbers:
                return x * number

        return -1

    def part_2 (self) -> int:
        numbers = list(self.numbers)
        for i1, n1 in enumerate(numbers):
            for _, n2 in enumerate(numbers, i1):
                x = self.GOAL - n1 - n2
                if x in self.numbers:
                    return n1 * n2 * x

        return -1

example = """1721
979
366
299
675
1456"""
puzzle = """"""

assert ReportRepair(example).part_1() == 514579
print("Part 1:", ReportRepair(puzzle).part_1())

assert ReportRepair(example).part_2() == 241861950
print("Part 2:", ReportRepair(puzzle).part_2())