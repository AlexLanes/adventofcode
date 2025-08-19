class PassagePathing:

    paths: dict[str, set[str]]

    def __init__ (self, s: str) -> None:
        self.paths = {}
        for line in s.split("\n"):
            a, b = line.split("-")
            if a not in self.paths:
                self.paths[a] = set()
            self.paths[a].add(b)
            if b not in self.paths:
                self.paths[b] = set()
            self.paths[b].add(a)

    def paths_possible (self) -> int:
        possible = 0
        paths = [["start"]]

        while paths:
            path = paths.pop(-1)
            last = path[-1]
            if last == "end":
                possible += 1
                continue

            for cave in self.paths[last]:
                if not (cave not in path or cave.isupper()):
                    continue
                paths.append([*path, cave])

        return possible

example = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
puzzle = """"""

assert PassagePathing(example).paths_possible() == 10
print("Part 1:", PassagePathing(puzzle).paths_possible())