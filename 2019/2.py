from typing import Self

example = "1,9,10,3,2,3,11,0,99,30,40,50"
puzzle_input = """1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,1,6,23,27,2,27,9,31,2,6,31,35,1,5,35,39,1,10,39,43,1,43,13,47,1,47,9,51,1,51,9,55,1,55,9,59,2,9,59,63,2,9,63,67,1,5,67,71,2,13,71,75,1,6,75,79,1,10,79,83,2,6,83,87,1,87,5,91,1,91,9,95,1,95,10,99,2,9,99,103,1,5,103,107,1,5,107,111,2,111,10,115,1,6,115,119,2,10,119,123,1,6,123,127,1,127,5,131,2,9,131,135,1,5,135,139,1,139,10,143,1,143,2,147,1,147,5,0,99,2,0,14,0"""

class ProgramAlarm:

    opcodes: list[int]

    def __init__ (self, s: str) -> None:
        self.opcodes = list(map(int, s.split(",")))

    def apply_state (self, noun: int, verb: int) -> Self:
        self.opcodes[1] = noun
        self.opcodes[2] = verb
        return self

    def handle_opcode_at (self, index: int) -> None:
        start, end = index + 1, index + 4
        match self.opcodes[index]:
            case 1:
                a, b, c = self.opcodes[start : end]
                self.opcodes[c] = self.opcodes[a] + self.opcodes[b]
            case 2:
                a, b, c = self.opcodes[start : end]
                self.opcodes[c] = self.opcodes[a] * self.opcodes[b]
            case _:
                raise IndexError()

    def run (self) -> int:
        index = 0
        while self.opcodes[index] != 99:
            self.handle_opcode_at(index)
            index += 4
        return self.opcodes[0]

    def run_find_output (self, output: int) -> int:
        original_opcodes = self.opcodes.copy()

        for noun in range(0, 100):
            for verb in range(0, 100):
                try:

                    self.apply_state(noun, verb)

                    index = 0
                    while self.opcodes[index] != 99:
                        self.handle_opcode_at(index)
                        index += 4

                    if self.opcodes[0] == output:
                        return 100 * noun + verb

                except IndexError: pass
                finally: self.opcodes = original_opcodes.copy()

        raise AssertionError("Not Found")

"""
`Opcode 1` adds together numbers read from two positions and stores the result in a third position.
The three integers immediately after the opcode tell you these three positions
The first two indicate the positions from which you should read the input values
Third indicates the position at which the output should be stored.

`Opcode 2` works exactly like opcode 1, except it multiplies the two inputs instead of adding them.
Again, the three integers after the opcode indicate where the inputs and outputs are, not their values.

Once you're done processing an opcode, move to the next one by stepping forward 4 positions.

`Opcode 99` means that the program is finished and should immediately halt

Encountering an unknown opcode means something went wrong.

---------------------------

Before running the program
Replace position 1 with the value 12
Replace position 2 with the value 2
What value is left at position 0 after the program halts?
"""
assert (value := ProgramAlarm(example).run()) == 3500, f"Unexpected '{value}'"
print("Part 1:", ProgramAlarm(puzzle_input).apply_state(12, 2).run())



"""
By replacing the values at addresses 1 (noun) and 2 (verb)
Each of the two input values will be between 0 and 99, inclusive.

Find the input noun and verb that cause the program to produce the output 19690720.
What is 100 * noun + verb?
"""
print("Part 2:", ProgramAlarm(puzzle_input).run_find_output(19690720))
