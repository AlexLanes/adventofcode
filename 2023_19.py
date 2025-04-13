from __future__ import annotations
from typing import Literal

class Part:

    x: int
    m: int
    a: int
    s: int

    def __init__ (self, part: str) -> None:
        parts = part.strip("{}").split(",")
        for attr, p in zip(self.__annotations__, parts):
            value = int(p.split("=")[1])
            setattr(self, attr, value)

    def __repr__ (self) -> str:
        return str(self.__dict__)

    def __iter__ (self):
        for attr in self.__annotations__:
            yield int(getattr(self, attr))

class Rule:

    part_name: Literal["x", "m", "a", "s"]
    operator: Literal["<", ">"]
    number: int
    true: str
    false: Rule | str

    def __init__ (self, rule: str) -> None:
        found = rule.find("{")
        if found != -1: rule = rule[found + 1 : -1]

        self.part_name, self.operator = rule[0 : 2] # type: ignore

        index = rule.index(":")
        self.number = int(rule[2 : index])

        index2 = rule.index(",", index)
        self.true = rule[index + 1 : index2]

        false = rule[index2 + 1 :]
        self.false = false if false.isalpha() else Rule(false)

    def __repr__ (self) -> str:
        return f"{self.part_name}{self.operator}{self.number}:{self.true},{self.false}"

    def apply (self, part: Part) -> str:
        val = getattr(part, self.part_name)
        if (val > self.number) if self.operator == ">" else (val < self.number):
            return self.true
        return self.false if isinstance(self.false, str) else self.false.apply(part)

class Aplenty:

    parts: list[Part]
    rules: dict[str, Rule]

    def __init__ (self, s: str) -> None:
        top, bottom = s.split("\n\n")
        self.parts = list(map(Part, bottom.split("\n")))

        self.rules = {}
        for rule in top.split("\n"):
            index = rule.index("{")
            name = rule[0 : index]
            self.rules[name] = Rule(rule[index :])

    def is_part_valid (self, part: Part) -> bool:
        current = "in"
        while current not in tuple("AR"):
            current = self.rules[current].apply(part)
        return current == "A"

    def valid_parts (self) -> list[Part]:
        return [
            part
            for part in self.parts
            if self.is_part_valid(part)
        ]

    def sum_of_valid_parts (self) -> int:
        return sum(map(sum, self.valid_parts()))

example = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
puzzle = """"""

assert Aplenty(example).sum_of_valid_parts() == 19114
print("Part 1:", Aplenty(puzzle).sum_of_valid_parts())