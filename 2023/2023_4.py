import re as regex

class Scratchcards:

    cards: dict[int, tuple[set[int], set[int]]]

    def __init__ (self, s: str) -> None:
        self.cards = {}
        spaces_re = regex.compile(r"\s+")

        for line in s.split("\n"):
            left, right = line.split(": ", 1)
            card_id = int(left.removeprefix("Card "))
            self.cards[card_id] = tuple(
                set(map(int, spaces_re.split(numbers.strip())))
                for numbers in right.split(" | ", 1)
            )

    def points_and_matches (self, card_id: int) -> tuple[int, int]:
        matches = points = 0
        numbers, winning_numbes = self.cards[card_id]

        for number in numbers:
            if number not in winning_numbes: continue
            points = (points * 2) or 1
            matches += 1

        return points, matches

    def total_points (self) -> int:
        return sum(
            self.points_and_matches(card)[0]
            for card in self.cards
        )

    def total_cards (self) -> int:
        cards_copies = { card: 1 for card in self.cards }
        def add_copies (card_id: int, matches: int) -> None:
            card_copies = cards_copies[card_id]
            for card in range(card_id + 1, card_id + matches + 1):
                if card not in self.cards: return
                cards_copies[card] += card_copies

        for card_id in self.cards:
            _, matches = self.points_and_matches(card_id)
            if not matches: continue
            add_copies(card_id, matches)

        return sum(cards_copies.values())

example = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
puzzle_input = """"""

"""
How many points are they worth in total?
you have to figure out which of the numbers you have appear in the list of winning numbers
you have to figure out which of the numbers you have (left) appear in the list of winning numbers (right)
The first match makes the card worth one point and each match after the first doubles the point value of that card.
"""
assert Scratchcards(example).total_points() == 13
print("Part 1:", Scratchcards(puzzle_input).total_points())

"""
How many total scratchcards do you end up with?
Process all of the original and copied scratchcards until no more scratchcards are won.
you win copies of the scratchcards below the winning card equal to the number of matches.
    - So, if card 10 were to have 5 matching numbers, you would win one copy each of cards 11, 12, 13, 14, and 15.
"""
assert Scratchcards(example).total_cards() == 30
print("Part 2:", Scratchcards(puzzle_input).total_cards())