from __future__ import annotations
from collections import Counter
from itertools import pairwise
from typing import Generator, Self

class Node[T]:

    value: T
    left: Node[T] | None
    right: Node[T] | None

    def __init__ (self, value: T) -> None:
        self.value = value
        self.left = self.right = None

    def __repr__(self) -> str:
        return str(self.value)

    def __iter__ (self) -> Generator[Node[T], None, None]:
        node: Node | None = self
        while node:
            yield node
            node = node.right

    def add_right (self, node: Node[T]) -> None:
        right = self.right
        self.right = node
        node.left = self
        node.right = right
        if right: right.left = node

class ExtendedPolymerization:

    head: Node[str]
    pairs: dict[str, str]

    def __init__ (self, s: str) -> None:
        template, pairs = s.split("\n\n")
        self.pairs = {
            k: v
            for pair in pairs.split("\n")
            for k, v in [pair.split(" -> ")]
        }

        head = Node("")
        node = head
        for char in template:
            n = Node(char)
            node.add_right(n)
            node = n
        assert head.right
        self.head = head.right

    def __str__ (self) -> str:
        return "".join(map(str, self.head))

    def n_step (self, n=1) -> Self:
        assert n >= 1

        for _ in range(n):
            for nodes in pairwise(self.head):
                pair = "".join(map(str, nodes))
                element = self.pairs.get(pair, None)
                if not element: continue
                nodes[0].add_right(Node(element))

        return self

    def most_minus_least (self) -> int:
        counter = Counter(node.value for node in self.head)
        most, *_, least = counter.most_common()
        return most[1] - least[1]

example = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""
puzzle = """HBHVVNPCNFPSVKBPPCBH

HV -> B
KS -> F
NH -> P
OP -> K
OV -> C
HN -> O
FF -> K
CP -> O
NV -> F
VB -> C
KC -> F
CS -> H
VC -> F
HF -> V
NK -> H
CF -> O
HH -> P
FP -> O
OH -> K
NN -> C
VK -> V
FB -> F
VP -> N
FC -> P
SV -> F
NO -> C
VN -> S
CH -> N
FN -> N
FV -> P
CN -> H
PS -> S
VF -> K
BN -> S
FK -> C
BB -> H
VO -> P
KN -> N
ON -> C
BO -> S
VS -> O
PK -> C
SK -> P
KF -> K
CK -> O
PB -> H
PF -> O
KB -> V
CC -> K
OK -> B
CV -> P
PO -> O
SH -> O
NP -> F
CO -> F
SS -> P
FO -> K
NS -> O
PN -> H
PV -> V
KP -> C
BK -> B
BP -> F
NB -> C
OF -> O
OC -> O
HO -> C
SC -> K
HC -> C
HS -> B
KH -> N
FS -> N
PH -> O
PC -> V
BS -> O
KO -> F
SP -> K
OB -> O
SF -> K
KV -> F
NC -> B
SO -> C
CB -> S
VH -> V
FH -> F
SN -> V
SB -> P
PP -> B
BF -> K
HB -> O
OO -> V
HP -> H
KK -> O
BV -> K
BH -> B
HK -> H
BC -> C
VV -> S
OS -> F
NF -> B"""

assert ExtendedPolymerization(example).n_step(10).most_minus_least() == 1588
print("Part 1:", ExtendedPolymerization(puzzle).n_step(10).most_minus_least())

# Timeout
# assert ExtendedPolymerization(example).n_step(40).most_minus_least() == 2188189693529
# print("Part 2:", ExtendedPolymerization(puzzle).n_step(40).most_minus_least())