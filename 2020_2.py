class PasswordPhilosophy:

    passwords: list[tuple[tuple[int, int], str, str]]

    def __init__ (self, s: str) -> None:
        self.passwords = []
        for a, b, c in map(str.split, s.splitlines()):
            low, high = map(int, a.split("-"))
            self.passwords.append((
                (low, high),
                b.removesuffix(":"),
                c
            ))

    def valid_passwords_1 (self) -> int:
        def is_valid (password: tuple[tuple[int, int], str, str]) -> bool:
            (low, high), letter, word = password
            count = word.count(letter)
            return low <= count <= high

        return sum(is_valid(password) for password in self.passwords)

    def valid_passwords_2 (self) -> int:
        def is_valid (password: tuple[tuple[int, int], str, str]) -> bool:
            low_high, letter, word = password
            return sum(
                1
                for index in map(lambda n: n - 1, low_high)
                if word[index] == letter
            ) == 1

        return sum(is_valid(password) for password in self.passwords)

example = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
puzzle = """"""

assert PasswordPhilosophy(example).valid_passwords_1() == 2
print("Part 1:", PasswordPhilosophy(puzzle).valid_passwords_1())

assert PasswordPhilosophy(example).valid_passwords_2() == 1
print("Part 2:", PasswordPhilosophy(puzzle).valid_passwords_2())