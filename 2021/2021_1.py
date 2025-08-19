from helpers import windows

class SonarSweep:

    measurements: list[int]

    def __init__ (self, s: str) -> None:
        self.measurements = list(map(int, s.split("\n")))

    def count_increases (self) -> int:
        return sum(
            1
            for left, right in windows(self.measurements)
            if right > left
        )

    def count_three_measurements (self) -> int:
        original = self.measurements

        self.measurements = [sum(group) for group in windows(original, size=3)]
        increases = self.count_increases()

        self.measurements = original
        return increases

example = """199
200
208
210
200
207
240
269
260
263"""
puzzle = """"""
assert SonarSweep(example).count_increases() == 7
assert SonarSweep(example).count_three_measurements() == 5
print("Part 1:", SonarSweep(puzzle).count_increases())
print("Part 2:", SonarSweep(puzzle).count_three_measurements())