puzzle_input = """90903
135889
120859
137397
56532
92489
87979
149620
137436
62999
71672
61022
139765
69690
109513
67615
77803
146519
96432
129440
67912
143886
126992
129921
122339
61684
149706
52779
106421
145896
145977
76585
136021
63976
97063
114899
118570
102196
129126
98521
136186
68054
72452
92433
145851
98487
149980
114477
125479
62351
131559
115553
129371
147164
83125
146200
68621
55982
79131
64907
95570
132347
76889
96461
123627
128180
113508
70342
139386
131234
140377
119825
80791
52090
62615
101366
138512
113752
77912
64447
146047
94578
82228
116731
123488
103839
120854
54663
129242
51587
149536
71096
110104
145155
139278
78799
62410
64645
112849
60402"""

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