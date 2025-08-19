"""
Analyze the unusual data from the engineers. How many reports are safe?
Safe:
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
"""

puzzle_input = """"""

from typing import Literal
type Report = list[int]

def type_of_report (report: Report) -> Literal["increasing", "decreasing", "unsafe"]:
    sorted_report: Report = sorted(report)
    if sorted_report == report: return "increasing"
    if list(reversed(report)) == sorted_report: return "decreasing"
    return "unsafe"

def validate_levels (report: Report) -> bool:
    for i in range(1, len(report)):
        current, prev = report[i], report[i - 1]
        diff = abs(current - prev)
        if diff == 0 or diff > 3: return False
    return True

def is_safe (report: Report) -> bool:
    def check (r: Report) -> bool:
        return type_of_report(r) != "unsafe" and validate_levels(r)

    # part 1
    if check(report): return True
    # part 2 - check all copies without 1 level
    for i in range(0, len(report)):
        copy: Report = [level for j, level in enumerate(report) if i != j]
        if check(copy): return True

    return False

# examples: list[tuple[Report, bool]] = [ # part 1
#     ([7, 6, 4, 2, 1], True),
#     ([1, 2, 7, 8, 9], False),
#     ([9, 7, 6, 2, 1], False),
#     ([1, 3, 2, 4, 5], False),
#     ([8, 6, 4, 4, 1], False),
#     ([1, 3, 6, 7, 9], True)
# ]
examples: list[tuple[Report, bool]] = [ # part 2
    ([7, 6, 4, 2, 1], True),
    ([1, 2, 7, 8, 9], False),
    ([9, 7, 6, 2, 1], False),
    ([1, 3, 2, 4, 5], True),
    ([8, 6, 4, 4, 1], True),
    ([1, 3, 6, 7, 9], True)
]

for report, safe in examples:
    print(f"Example {report=} {safe=} | type={type_of_report(report)}")
    assert is_safe(report) == safe
print("OK Examples")

reports: list[Report] = [
    [int(number) for number in line.strip().split(" ")]
    for line in puzzle_input.split("\n")
    if line
]
safe_reports = sum(1 for report in reports if is_safe(report))
print("Safe Reports: ", safe_reports)