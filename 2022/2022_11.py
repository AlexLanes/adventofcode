from functools import reduce

class Monkey:

    number: int
    items: list[int]
    operation: tuple[str, str] # (* | +, by | old)
    test: tuple[int, int, int] # (divisible by, true monkey, false monkey)
    inspections: int # quantity of inspections

    MULT_OF_ALL_TESTS = 1

    def __init__ (self, s: str) -> None:
        lines = s.split("\n")

        self.number = int(lines[0].split(" ")[1].rstrip(":"))
        self.inspections = 0
        self.items = [int(num) for num in lines[1].split(": ")[1].split(", ")]

        sign, by = lines[2].split("old ", 1)[1].split(" ")
        self.operation = (sign, by)

        by, true, false = (int(lines[i].rsplit(" ", 1)[-1]) for i in range(3, 6))
        self.test = (by, true, false)

        Monkey.MULT_OF_ALL_TESTS *= by

    def __repr__ (self) -> str:
        return str(self.__dict__)

    def __hash__ (self) -> int:
        return self.number

    def __eq__ (self, value: object) -> bool:
        return hash(self) == hash(value)

    def do_operation (self, item: int) -> int:
        """`Item` change"""
        sign = self.operation[0]
        by = int(self.operation[1]) if self.operation[1] != "old" else item
        return (item * by) if sign == "*" else (item + by)

    def do_test (self, item: int) -> int:
        """Test `item` and throw to monkey `int`"""
        by, true, false = self.test
        return true if item % by == 0 else false

    def throw (self, item: int) -> None:
        self.items.append(item)

class MonkeyInTheMiddle:

    monkeys: dict[int, Monkey]

    def __init__ (self, s: str) -> None:
        self.monkeys = {
            monkey.number: monkey
            for part in s.split("\n\n")
            if (monkey := Monkey(part))
        }

    def print (self) -> None:
        print(*self.monkeys.values(), sep="\n")

    def n_rounds (self, n=1, part=1) -> "MonkeyInTheMiddle":
        def once () -> None:
            for monkey in self.monkeys.values():
                while monkey.items:
                    monkey.inspections += 1
                    item = monkey.do_operation(monkey.items.pop(0))
                    item = (item // 3) if part == 1 else item % monkey.MULT_OF_ALL_TESTS
                    destination_monkey = monkey.do_test(item)
                    self.monkeys[destination_monkey].throw(item)

        for _ in range(n): once()
        return self

    def n_monkey_business (self, n=2) -> int:
        n_active_monkeys = sorted(
            self.monkeys.values(),
            key = lambda m: m.inspections,
            reverse = True
        )[0 : n]
        return reduce(
            lambda num, monkey: num * monkey.inspections,
            n_active_monkeys,
            1
        )

example = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""
puzzle = """"""

assert MonkeyInTheMiddle(example).n_rounds(20).n_monkey_business() == 10605
print("Part 1:", MonkeyInTheMiddle(puzzle).n_rounds(20).n_monkey_business())

assert MonkeyInTheMiddle(example).n_rounds(10_000, part=2).n_monkey_business() == 2713310158
print("Part 2:", MonkeyInTheMiddle(puzzle).n_rounds(10_000, part=2).n_monkey_business())