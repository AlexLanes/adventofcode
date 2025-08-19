"""
Scan the corrupted memory for uncorrupted mul instructions.
What do you get if you add up all of the results of the multiplications
Multiplications:
    mul(X,Y)
"""

puzzle_input = """"""

import re as regex
from collections import deque as Deque

mul_re = regex.compile(r"mul\(\d+,\d+\)")
# mul_parts: list[str] = mul_re.findall(puzzle_input)

def part_multiply (part: str) -> int:
    left, right = map(
        lambda p: int("".join(char for char in p if char.isdigit())),
        part.split(",")
    )
    return left * right

# print("Add all Multiplications: ", sum(
#     part_multiply(part)
#     for part in mul_parts
# ))



# --- Part Two ---
do_or_dont_re = regex.compile(r"don't\(\)|do\(\)")
do_or_dont_start_positions = Deque(
    ("don't" not in match.group(), match.start())
    for match in do_or_dont_re.finditer(puzzle_input)
)
mul_parts_start_positions = [
    (match.group(), match.start())
    for match in mul_re.finditer(puzzle_input)
]

result = 0
is_do, do_dont_start = do_or_dont_start_positions.popleft()

for part, part_start_position in mul_parts_start_positions:
    while do_or_dont_start_positions and do_or_dont_start_positions[0][1] < part_start_position:
        is_do, do_dont_start = do_or_dont_start_positions.popleft()

    if not is_do: continue
    mul = part_multiply(part)
    result += mul

print("Add all Multiplications: ", result)
