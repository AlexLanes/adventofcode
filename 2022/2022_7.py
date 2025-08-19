from __future__ import annotations
from functools import cached_property
from pathlib import PurePath
from typing import Generator

class File:

    path: PurePath
    size: int

    def __init__ (self, path: PurePath, size: int) -> None:
        self.size = size
        self.path = path

    def __repr__ (self) -> str:
        return f"""<File "{self.path}" | {self.size} size>"""

    def __hash__ (self) -> int:
        return hash(self.path)

    def __eq__ (self, value: object) -> bool:
        return hash(self) == hash(value)

class Dir:

    path: PurePath
    parent: Dir | None
    files: list[File]
    dirs: list[Dir]

    def __init__ (self, path: PurePath, parent: Dir | None = None) -> None:
        self.files, self.dirs = [], []
        self.path, self.parent = path, parent

    def __repr__ (self) -> str:
        return f"""<Dir "{self.path}" | {len(self.files)} files | {len(self.dirs)} dirs>"""

    def __hash__ (self) -> int:
        return hash(self.path)

    def __eq__ (self, value: object) -> bool:
        return hash(self) == hash(value)

    @cached_property
    def size (self) -> int:
        files = sum(file.size for file in self.files)
        return files + sum(d.size for d in self.dirs)

    def all_dirs (self) -> Generator[Dir, None, None]:
        yield self
        for d in self.dirs:
            yield from d.all_dirs()

class Parser:

    root: Dir
    lines: list[str]
    index: int

    TOTAL_SPACE = 70_000_000
    SPACE_NEEDED = 30_000_000

    def __init__ (self, s: str) -> None:
        self.root = Dir(PurePath("/"))
        self.index = 0
        _, *self.lines = s.split("\n")
        self.parse()

    def end (self) -> bool:
        return self.index >= len(self.lines)

    def line (self) -> str:
        return self.lines[self.index]

    def handle_ls (self, root: Dir) -> None:
        self.index += 1 # consume `$ ls`
        while not self.end() and not self.line().startswith("$"):
            left, right = self.line().split(" ")
            path = root.path / right

            if left == "dir": root.dirs.append(Dir(path, root))
            else: root.files.append(File(path, int(left)))

            self.index += 1 # next

    def handle_cd (self, root: Dir) -> Dir:
        line = self.line()
        self.index += 1 # consume `$ cd`

        if line.endswith(".."):
            assert root.parent
            return root.parent

        _, _, name = line.split(" ")
        index = root.dirs.index(Dir(root.path / name))
        return root.dirs[index]

    def parse (self) -> "Parser":
        root = self.root

        while not self.end():
            match self.line():
                case line if line == "$ ls": self.handle_ls(root)
                case line if line.startswith("$ cd"): root = self.handle_cd(root)
                case _: raise Exception(f"Line not expected '{line}'")

        return self

    def sum_dirs_at_most (self, size=100_000) -> int:
        return sum(
            d.size
            for d in self.root.all_dirs()
            if d.size <= size
        )

    def smallest_dir_to_space_needed (self) -> Dir:
        unused_space = self.TOTAL_SPACE - self.root.size
        space_to_free = self.SPACE_NEEDED - unused_space
        ordered_size_dirs = sorted(self.root.all_dirs(), key=lambda d: d.size)

        for d in ordered_size_dirs:
            if d.size > space_to_free:
                return d

        raise Exception("Not Found")

example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""
puzzle = """"""

assert Parser(example).sum_dirs_at_most() == 95_437
print("Part 1:", Parser(puzzle).sum_dirs_at_most())

assert Parser(example).root.size == 48381165
assert Parser(example).smallest_dir_to_space_needed().size == 24933642
print("Part 2:", Parser(puzzle).smallest_dir_to_space_needed().size)