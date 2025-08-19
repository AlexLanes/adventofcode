import functools, operator

class MonkeyMath:

    type Expression = tuple[str, str, str]
    "`(digits or name, operator, digits or name)`"
    jobs: dict[str, Expression]

    OPERATORS = { "+": operator.add, "-": operator.sub,
                  "*": operator.mul, "/": operator.floordiv }

    def __init__ (self, s: str) -> None:
        self.jobs = {}
        for line in s.split("\n"):
            name, expression = line.split(": ", 1)
            if expression.isdigit(): expression += " + 0"
            left, operator, right = expression.split(" ", 2)
            self.jobs[name] = (left, operator, right)

    @functools.cache
    def value (self, job: str) -> int:
        assert job in self.jobs
        left, operator, right = self.jobs[job]
        return self.OPERATORS[operator](
            int(left) if left.isdigit() else self.value(left),
            int(right) if right.isdigit() else self.value(right),
        )

example = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""
puzzle = """"""

assert MonkeyMath(example).value("root") == 152
print("Part 1:",  MonkeyMath(puzzle).value("root"))