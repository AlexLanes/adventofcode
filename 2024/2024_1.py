"""
What is the total distance between your lists?
To find the total distance between the left list and the right list, add up the distances between all of the pairs you found
Pair up the numbers and measure how far apart they are.
    Pair up the smallest number in the left list with the smallest number in the right list,
    then the second-smallest left number with the second-smallest right number,
    and so on
"""

puzzle_input = """"""

# import bisect

# sorted_left: list[int] = []
# sorted_right = sorted_left.copy()
# for line in puzzle_input.split("\n"):
#     line = line.strip()
#     if not line: continue

#     l, r = map(int, line.replace("   ", ",", 1).split(","))
#     bisect.insort(sorted_left, l)
#     bisect.insort(sorted_right, r)

# print("Total Distance: ", sum(
#     abs(l - r)
#     for l, r in zip(sorted_left, sorted_right)
# ))



"""
Part 2
This time, you'll need to figure out exactly how often each number from the left list appears in the right list.
Calculate a total similarity score by adding up each number in the left list after multiplying it
by the number of times that number appears in the right list.
"""

from collections import defaultdict

left: list[int] = []
right: defaultdict[int, int] = defaultdict(int)
for line in puzzle_input.split("\n"):
    line = line.strip()
    if not line: continue

    l, r = map(int, line.replace("   ", ",", 1).split(","))
    left.append(l)
    right[r] += 1

print("Similarity Score: ", sum(
    num * right[num]
    for num in left
))