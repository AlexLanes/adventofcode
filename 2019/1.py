puzzle_input = """"""

class RocketEquation:

    modules_mass: list[int]

    def __init__ (self, s: str) -> None:
        self.modules_mass = [
            int(line)
            for line in s.splitlines()
        ]

    def fuel_required (self, mass: int) -> int:
        return max(0, mass // 3 - 2)

    def total_fuel_requirement (self) -> int:
        return sum(map(self.fuel_required, self.modules_mass))

    def total_fuel_requirement_2 (self) -> int:
        total = 0

        for mass in self.modules_mass:
            fuel_mass = self.fuel_required(mass)
            total += fuel_mass
            while fuel_mass := self.fuel_required(fuel_mass):
                total += fuel_mass

        return total

"""
At the first Go / No Go poll, every Elf is Go until the Fuel Counter-Upper.
They haven't determined the amount of fuel required yet.

Fuel required to launch a given module is based on its mass.

Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

The Fuel Counter-Upper needs to know the total fuel requirement.
To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.
"""
rocket = RocketEquation(puzzle_input)
print("Part 1:", rocket.total_fuel_requirement())

"""
For each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative

(Calculate the fuel requirements for each module separately, then add them all up at the end.)
"""
print("Part 2:", rocket.total_fuel_requirement_2())