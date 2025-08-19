class BinaryDiagnostic:

    reports: list[list[int]]

    def __init__ (self, s: str) -> None:
        self.reports = [
            list(map(int, line))
            for line in s.split("\n")
        ]

    def power_consumption (self) -> int:
        reports = self.reports
        gamma_rate: list[str] = []
        epsilon_rate = gamma_rate.copy()

        for col in range(len(reports[0])):
            bit = 1 if sum(report[col] or -1 for report in reports) > 0 else 0
            gamma_rate.append(str(bit))
            epsilon_rate.append("1" if bit == 0 else "0")

        return int("".join(gamma_rate), 2) * int("".join(epsilon_rate), 2)

example = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""
puzzle = """"""

assert BinaryDiagnostic(example).power_consumption() == 198
print("Part 1:", BinaryDiagnostic(puzzle).power_consumption())