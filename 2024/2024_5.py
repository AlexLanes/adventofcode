"""
Determine which updates are already in the correct order.
What do you get if you add up the middle page number from those correctly-ordered updates?
"""

example = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""
puzzle_input = """"""

class Queue:

    ordering_rules: dict[int, list[int]]
    updates: list[list[int]]

    def __init__ (self, s: str) -> None:
        rules, updates = s.split("\n\n", 1)

        self.updates = [
            [*map(int, update.split(","))]
            for update in updates.split("\n")
        ]

        self.ordering_rules = {}
        for rule in rules.split("\n"):
            left, right = map(int, rule.split("|"))
            if left not in self.ordering_rules:
                self.ordering_rules[left] = []
            self.ordering_rules[left].append(right)

    def is_valid (self, update: list[int]) -> bool:
        seen: set[int] = set()

        for num in update:
            order = self.ordering_rules.get(num, [])
            invalid = any(s in order for s in seen)
            if invalid: return False
            seen.add(num)

        return True

    def sum_middle_of_valids (self) -> int:
        _sum = 0
        for update in self.updates:
            if not self.is_valid(update): continue
            middle = update[len(update) // 2]
            _sum += middle
        return _sum

    def correct_update (self, update: list[int]) -> None:
        left = 0
        while left < len(update) - 1:

            for right in range(left + 1, len(update)):
                if update[left] in self.ordering_rules.get(update[right], []):
                    update[left], update[right] = update[right], update[left]

            left += 1

    def sum_middle_of_invalids (self) -> int:
        _sum = 0
        for update in self.updates:
            if self.is_valid(update): continue
            self.correct_update(update)
            middle = update[len(update) // 2]
            _sum += middle
        return _sum

assert Queue(example).sum_middle_of_valids() == 143
# print(Queue(puzzle_input).sum_middle_of_valids())


"""
--- Part 2 ---
What do you get if you add up the middle page numbers after
correctly ordering only the incorrectly-ordered updates?
"""

assert Queue(example).sum_middle_of_invalids() == 123
print(Queue(puzzle_input).sum_middle_of_invalids())