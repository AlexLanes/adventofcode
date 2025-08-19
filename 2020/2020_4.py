import string, typing
import re as regex

class PassportProcessing:

    passwords: list[dict[str, str]]
    REQUIRED_FIELDS_VALIDATION: dict[str, typing.Callable[[str], bool]] = {
        "byr": lambda x: len(x) == 4 and x.isdigit() and 1920 <= int(x) <= 2002,
        "iyr": lambda x: len(x) == 4 and x.isdigit() and 2010 <= int(x) <= 2020,
        "eyr": lambda x: len(x) == 4 and x.isdigit() and 2020 <= int(x) <= 2030,
        "hgt": lambda x: regex.match(r"\d+(in|cm)", x) != None
                         and any((
                             x.removesuffix("in").isdigit() and 59  <= int(x.removesuffix("in")) <= 76,
                             x.removesuffix("cm").isdigit() and 150 <= int(x.removesuffix("cm")) <= 193,
                         )),
        "hcl": lambda x: len(x) == 7 and x.startswith("#")
                         and sum(1 for char in x if char in string.hexdigits) == 6,
        "ecl": lambda x: x in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": lambda x: len(x) == 9 and x.isdigit(),
    }

    def __init__ (self, s: str) -> None:
        self.passwords = [
            {
                key: value            
                for line in passport.splitlines()
                for part in line.split()
                for key, value in [part.split(":")]
            }
            for passport in s.split("\n\n") 
        ]

    def part_1 (self) -> int:
        return sum(
            1
            for password in self.passwords
            if all(field in password
                   for field in self.REQUIRED_FIELDS_VALIDATION)
        )

    def part_2 (self) -> int:
        def is_valid (password: dict[str, str]) -> bool:
            for field, validation in self.REQUIRED_FIELDS_VALIDATION.items():
                if field not in password: return False
                try:
                    value = password[field]
                    if not validation(value): return False
                except: return False
            return True

        return sum(
            1
            for password in self.passwords
            if is_valid(password)
        )

example = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""
puzzle = """"""

assert PassportProcessing(example).part_1() == 2
print("Part 1:", PassportProcessing(puzzle).part_1())

assert PassportProcessing(example).part_2() == 2
print("Part 2:", PassportProcessing(puzzle).part_2())