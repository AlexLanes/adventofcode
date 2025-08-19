class Ranges:

    type Range = tuple[int, int, int]
    """`(destination, source, length)`"""
    ranges: list[Range]

    def __init__ (self, ranges: list[str]) -> None:
        self.ranges = [
            tuple(int(num) for num in _range.split(" "))
            for _range in ranges
        ]

    def __repr__ (self) -> str:
        names = ("destination", "source", "length")
        return str([
            f"<Range {
                " ".join(f"{name}={num}"
                for num, name in zip(_range, names))
            }>"
            for _range in self.ranges
        ]).replace("'", "")

    def convert (self, number: int) -> int:
        for destination, source, length in self.ranges:
            if source <= number < source + length:
                delta = number - source
                return destination + delta
        return number

class Almanac:

    seeds: list[int]
    maps_ranges: list[Ranges] # [ranges of map1, ranges of map2, ...]

    def __init__ (self, s: str) -> None:
        seeds, s = s.split("\n\n", 1)
        self.seeds = [
            int(seed)
            for seed in seeds.split(": ")[1].split(" ")
        ]

        self.maps_ranges = []
        for maps in s.split("\n\n"):
            ranges = Ranges(maps.split("\n")[1 : ])
            self.maps_ranges.append(ranges)

    def seed_location (self, seed: int) -> int:
        number = seed
        for ranges in self.maps_ranges:
            number = ranges.convert(number)
        return number

    def lowest_seed_location (self) -> int:
        return min(
            self.seed_location(seed)
            for seed in self.seeds
        )

"""
What is the lowest location number that corresponds to any of the initial seed numbers?
    - The almanac starts by listing which seeds need to be planted
    - The rest of the almanac contains a list of maps which describe how to
        convert numbers from a source category into numbers in a destination category
    - Each line within a map contains three numbers:
        - the destination range start [0]
        - the source range start [1]
        - the range length [2]
    - Any source numbers that aren't mapped correspond to the same destination number
"""

example = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
puzzle_input = """"""

assert Almanac(example).lowest_seed_location() == 35
print("Part 1:", Almanac(puzzle_input).lowest_seed_location())