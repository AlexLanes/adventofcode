from collections import deque

class Lanternfish:

    adults: deque[int]
    "`[0..6]`"
    news: deque[int]
    "`[7, 8]`"

    def __init__ (self, s: str) -> None:
        self.news, self.adults = (deque([0] * n, maxlen=n) for n in (2, 7))
        for num in map(int, s.split(",")):
            self.adults[num] += 1

    def update_one_day (self) -> None:
        zeros = self.adults.popleft()
        sevens = self.news.popleft()
        to_six = sevens + zeros
        self.adults.append(to_six)
        self.news.append(zeros)

    def sum_after_n_days (self, days=80) -> int:
        for _ in range(days): self.update_one_day()
        return sum(self.adults) + sum(self.news)

example = "3,4,3,1,2"
puzzle = "1,1,5,2,1,1,5,5,3,1,1,1,1,1,1,3,4,5,2,1,2,1,1,1,1,1,1,1,1,3,1,1,5,4,5,1,5,3,1,3,2,1,1,1,1,2,4,1,5,1,1,1,4,4,1,1,1,1,1,1,3,4,5,1,1,2,1,1,5,1,1,4,1,4,4,2,4,4,2,2,1,2,3,1,1,2,5,3,1,1,1,4,1,2,2,1,4,1,1,2,5,1,3,2,5,2,5,1,1,1,5,3,1,3,1,5,3,3,4,1,1,4,4,1,3,3,2,5,5,1,1,1,1,3,1,5,2,1,3,5,1,4,3,1,3,1,1,3,1,1,1,1,1,1,5,1,1,5,5,2,1,5,1,4,1,1,5,1,1,1,5,5,5,1,4,5,1,3,1,2,5,1,1,1,5,1,1,4,1,1,2,3,1,3,4,1,2,1,4,3,1,2,4,1,5,1,1,1,1,1,3,4,1,1,5,1,1,3,1,1,2,1,3,1,2,1,1,3,3,4,5,3,5,1,1,1,1,1,1,1,1,1,5,4,1,5,1,3,1,1,2,5,1,1,4,1,1,4,4,3,1,2,1,2,4,4,4,1,2,1,3,2,4,4,1,1,1,1,4,1,1,1,1,1,4,1,5,4,1,5,4,1,1,2,5,5,1,1,1,5"

assert Lanternfish(example).sum_after_n_days() == 5934
assert Lanternfish(example).sum_after_n_days(256) == 26984457539
print("Part 1:", Lanternfish(puzzle).sum_after_n_days())
print("Part 2:", Lanternfish(puzzle).sum_after_n_days(256))