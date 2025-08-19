class TheTreacheryOfWhales:

    positions: list[int]

    def __init__ (self, s: str) -> None:
        self.positions = list(map(int, s.split(",")))

    def min_fuel_to_align (self) -> int:
        min_fuel = 999999999
        seen: set[int] = set()

        for position in self.positions:
            if position in seen: continue
            fuel = sum(abs(position - p)
                       for p in self.positions)
            min_fuel = min(min_fuel, fuel)
            seen.add(position)

        return min_fuel

example = "16,1,2,0,4,2,7,1,2,14"
puzzle = ""

assert TheTreacheryOfWhales(example).min_fuel_to_align() == 37
print("Part 1:", TheTreacheryOfWhales(puzzle).min_fuel_to_align())