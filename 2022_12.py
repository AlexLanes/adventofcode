from collections import deque
from helpers import Grid, Position

class HillClimbingAlgorithm:

    grid: Grid[int]
    start: Position
    end: Position

    def __init__ (self, s: str) -> None:
        grid: list[list[int]] = []
        transformations = { "S": "a", "E": "z" }

        for r, line in enumerate(s.split("\n")):
            row = []

            for c, char in enumerate(line):
                if char == "S": self.start = Position(r, c)
                elif char == "E": self.end = Position(r, c)
                value = ord(transformations.get(char, char))
                row.append(value)

            grid.append(row)

        self.grid = Grid(grid)

    def can_go_to_adjacent (self, position: Position, destination: Position) -> bool:
        if not all(self.grid.in_bounds(p) for p in (position, destination)):
            return False
        return self.grid[destination] - 1 <= self.grid[position]

    def fewest_steps_from_start (self) -> int:
        seen, dq = set(), deque([(self.start, 0)])

        while dq:
            current, steps = dq.popleft()

            if current == self.end: return steps
            if current in seen: continue

            seen.add(current)
            for adjacent in current.adjacents(diagonals=False):
                if adjacent in seen or not self.can_go_to_adjacent(current, adjacent):
                    continue
                dq.append((adjacent, steps + 1))

        return -1

    def fewest_steps_from_any_a (self) -> int:
        start = self.start
        a, fewest = ord("a"), 999999999

        for position in self.grid:
            if self.grid[position] != a: continue
            self.start = position
            if (result := self.fewest_steps_from_start()) != -1:
                fewest = min(fewest, result)

        self.start = start
        return fewest

example = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""
puzzle = """abacccaaaacccccccccccaaaaaacccccaaaaaaccccaaacccccccccccccccccccccccccccccccccccccccccccaaaaa
abaaccaaaacccccccccccaaaaaaccccccaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccccccaaaaa
abaaccaaaacccccccccccaaaaacccccaaaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccccccaaaaa
abccccccccccccccccccccaaaaacccaaaaaaaaaaaaaaaacccccccccccccccccccccccccccaaaccccccccccccaaaaa
abccccccccccccccccccccaacaacccaaaaaaaaccaaaaaccccccccccccccccccccccccccccaaaccccccccccccaccaa
abcccccccccccccaacccaaaccccccaaaaaaaaaccaaaaaccccccccccccccccccccccccccccccacccccccccccccccca
abcccccccccccaaaaaaccaaaccacccccaaaaaaacccccccccccccccccccccccccciiiicccccccddddddccccccccccc
abcccccccccccaaaaaaccaaaaaaaccccaaaaaacccccaacccccccaaaccccccccciiiiiiiicccdddddddddacaaccccc
abccccccccccccaaaaaaaaaaaaacccccaaaaaaacaaaacccccccaaaacccccccchhiiiiiiiiicddddddddddaaaccccc
abcccccccccccaaaaaaaaaaaaaacccccccaaacccaaaaaacccccaaaaccccccchhhipppppiiiijjjjjjjddddaaccccc
abcccccccccccaaaaaaaaaaaaaaccccccccccccccaaaaaccccccaaaccccccchhhpppppppiijjjjjjjjjddeeaccccc
abcccccccccccccccccaaaaaaaacccccccccccccaaaaaccccccccccccccccchhppppppppppjjqqqjjjjjeeeaacccc
abccccccccccccccccccaaaaaaaacccccccccccccccaacccccccccccccccchhhpppuuuupppqqqqqqqjjjeeeaacccc
abcccccccccccccccccccaacccacccccccccccccccccccccccccccccccccchhhopuuuuuuppqqqqqqqjjjeeecccccc
abacccccccccccccaaacaaaccccccccccccccccccccccccccccaaccccccchhhhoouuuuuuuqvvvvvqqqjkeeecccccc
abaccccccccccccaaaaaacccccaaccccccccccccccccccccccaaaccccccchhhooouuuxxxuvvvvvvqqqkkeeecccccc
abaccccccccccccaaaaaacccaaaaaaccccccccccccccccccaaaaaaaaccchhhhooouuxxxxuvyyyvvqqqkkeeecccccc
abcccccccccccccaaaaacccaaaaaaaccccccccccccccccccaaaaaaaaccjjhooooouuxxxxyyyyyvvqqqkkeeecccccc
abccccccccccccccaaaaaacaaaaaaaccccccccaaaccccccccaaaaaaccjjjooootuuuxxxxyyyyyvvqqkkkeeecccccc
abccccccccccccccaaaaaaaaaaaaacccccccccaaaacccccccaaaaaacjjjooootttuxxxxxyyyyvvrrrkkkeeecccccc
SbccccccccccccccccccaaaaaaaaacccccccccaaaacccccccaaaaaacjjjoootttxxxEzzzzyyvvvrrrkkkfffcccccc
abcccccccccccaaacccccaaaaaaacaaaccccccaaaccccccccaaccaacjjjoootttxxxxxyyyyyyvvvrrkkkfffcccccc
abcccccccccaaaaaacccaaaaaacccaaacacccaacccccccccccccccccjjjoootttxxxxyxyyyyyywvvrrkkkfffccccc
abcccccccccaaaaaacccaaaaaaaaaaaaaaaccaaacaaacccccaacccccjjjnnnttttxxxxyyyyyyywwwrrkkkfffccccc
abcaacacccccaaaaacccaaacaaaaaaaaaaaccaaaaaaacccccaacaaacjjjnnnntttttxxyywwwwwwwwrrrlkfffccccc
abcaaaaccccaaaaacccccccccaacaaaaaaccccaaaaaacccccaaaaacccjjjnnnnnttttwwywwwwwwwrrrrllfffccccc
abaaaaaccccaaaaaccccccaaaaaccaaaaacaaaaaaaaccccaaaaaaccccjjjjinnnntttwwwwwsssrrrrrllllffccccc
abaaaaaaccccccccccccccaaaaacaaaaaacaaaaaaaaacccaaaaaaacccciiiiinnnntswwwwssssrrrrrlllfffccccc
abacaaaaccccccccccccccaaaaaacaaccccaaaaaaaaaaccccaaaaaaccccciiiinnnssswwsssssllllllllfffccccc
abccaaccccccccccccccccaaaaaaccccccccccaaacaaaccccaaccaacccccciiiinnsssssssmmllllllllfffaacccc
abccccccccccccccccccccaaaaaaccccccccccaaaccccccccaaccccccccccciiinnmsssssmmmmlllllgggffaacccc
abcccccccccccccccaccccccaaacccccccccccaaccccccccccccccccccccccciiimmmsssmmmmmgggggggggaaacccc
abcccccccccaaaaaaaaccccccccccccccccccccccccccccaaaaaccccccccccciiimmmmmmmmmgggggggggaaacccccc
abccccccccccaaaaaaccccccccccccccccccaacccccccccaaaaacccccccccccciiimmmmmmmhhggggcaaaaaaaccccc
abccccccccccaaaaaacccccccccccccccccaacccccccccaaaaaacccccccccccciihhmmmmhhhhgccccccccaacccccc
abccccaacaaaaaaaaaaccccccccccccccccaaaccccccccaaaaaaccccccccccccchhhhhhhhhhhaaccccccccccccccc
abccccaaaaaaaaaaaaaaccccccccccaaccaaaaccccccccaaaaaacccaaacccccccchhhhhhhhaaaaccccccccccccccc
abcccaaaaaaaaaaaaaaaccccccccaaaaaacaaaacacaccccaaaccccaaaacccccccccchhhhccccaaccccccccccaaaca
abcccaaaaaacacaaacccccccccccaaaaaaaaaaaaaaacccccccccccaaaacccccccccccaaaccccccccccccccccaaaaa
abcccccaaaacccaaaccccccccccaaaaaaaaaaaaaaaaccccccccccccaaacccccccccccaaacccccccccccccccccaaaa
abcccccaacccccaacccccccccccaaaaaaaaaaaaaccccccccccccccccccccccccccccccccccccccccccccccccaaaaa"""

assert HillClimbingAlgorithm(example).fewest_steps_from_start() == 31
print("Part 1:", HillClimbingAlgorithm(puzzle).fewest_steps_from_start())

assert HillClimbingAlgorithm(example).fewest_steps_from_any_a() == 29
print("Part 2:", HillClimbingAlgorithm(puzzle).fewest_steps_from_any_a())