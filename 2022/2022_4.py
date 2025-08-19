class CampCleanup:

    type Range = tuple[int, int]
    type Section = tuple[Range, Range]
    sections: list[Section]

    def __init__ (self, s: str) -> None:
        self.sections = []
        for left, right in (line.split(",", 1) for line in s.split("\n")):
            l1, l2, *_ = map(int, left.split("-", 1))
            r1, r2, *_ = map(int, right.split("-", 1))
            self.sections.append(((l1, l2), (r1, r2)))

    def is_super_set (self, section: Section) -> bool:
        return any(
            a[0] <= b[0] and a[1] >= b[1]
            for a, b in (section, reversed(section))
        )

    def count_super_set (self) -> int:
        return sum(
            1
            for section in self.sections
            if self.is_super_set(section)
        )

    def is_overlap (self, section: Section) -> bool:
        return any(
            b[0] <= a[0] <= b[1]
            for a, b in (section, reversed(section))
        )

    def count_overlap (self) -> int:
        return sum(
            1
            for section in self.sections
            if self.is_overlap(section)
        )

example = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""
puzzle_input = """"""

assert CampCleanup(example).count_super_set() == 2
print("Part 1:", CampCleanup(puzzle_input).count_super_set())

assert CampCleanup(example).count_overlap() == 4
print("Part 2:", CampCleanup(puzzle_input).count_overlap())