from functools import reduce

class GameCubes:

    games: dict[int, list[list[tuple[int, str]]]]
    max_cubes = {
        "red":   12,
        "blue":  14,
        "green": 13,
    }

    def __init__ (self, s: str) -> None:
        self.games = {}
        for line in s.split("\n"):
            left, right = line.split(": ")
            game_id = int(left.removeprefix("Game "))
            self.games[game_id] = [
                [
                    tuple(
                        int(x) if x.isdigit() else x
                        for x in _set.split(" ")
                    )
                    for _set in sets.split(", ")
                ]
                for sets in right.split("; ")
            ]

    def is_game_possible (self, game_id: int) -> bool:
        sets = self.games[game_id]
        for _set in sets:
            cubes = self.max_cubes.copy()

            for num, cube in _set:
                cubes[cube] -= num
            if any(value < 0 for value in cubes.values()): return False

        return True

    def sum_possible_games (self) -> int:
        return sum(
            game
            for game in self.games
            if self.is_game_possible(game)
        )

    def minimum_cubes_needed (self, game_id: int) -> dict[str, int]:
        minimum = {
            cube: -1
            for cube in self.max_cubes
        }

        for _set in self.games[game_id]:
            for num, cube in _set:
                m = max(num, minimum[cube])
                minimum[cube] = m

        return minimum

    def sum_power_of_minimum_cubes (self) -> int:
        mult = lambda a, b: a * b
        return sum(
            reduce(mult, self.minimum_cubes_needed(game_id).values())
            for game_id in self.games
        )

example = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
puzzle_input = """"""

"""
What is the sum of the IDs of those games?
Determine which games would have been possible if the bag had been loaded with only
    - 12 red cubes
    - 13 green cubes
    - 14 blue cubes
Cubes are replenishable
"""
assert GameCubes(example).sum_possible_games() == 8
print("Part 1:", GameCubes(puzzle_input).sum_possible_games())

"""
For each game, find the minimum set of cubes that must have been present.
Power the minimum set of cubes and add all games
"""
assert GameCubes(example).sum_power_of_minimum_cubes() == 2286
print("Part 2:", GameCubes(puzzle_input).sum_power_of_minimum_cubes())