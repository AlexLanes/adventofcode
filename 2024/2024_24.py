class CrossedWires:

    wires: dict[str, int]
    gates: dict[str, tuple[str, str, str]]

    def __init__ (self, s: str) -> None:
        top, bottom = s.split("\n\n")

        self.wires = {
            wire: int(val)
            for wire, val in (line.split(": ")
                              for line in top.split("\n"))
        }

        self.gates = {}
        for gate in bottom.split("\n"):
            left, op, right, _, output = gate.split(" ")
            self.gates[output] = (left, op, right)

        self.map_gates()

    def map_gates (self) -> None:
        def map_gate_output (gate: str, left: str, op: str, right: str) -> int:
            if gate in self.wires:
                return self.wires[gate]

            l, r = (self.wires[g] if g in self.wires else map_gate_output(g, *self.gates[g])
                    for g in (left, right))
            gate_value = (l or r) if op == "OR"\
                else (l and r) if op == "AND"\
                else int(l + r == 1)

            self.wires[gate] = gate_value
            return gate_value

        for gate, data in self.gates.items():
            map_gate_output(gate, *data)

    def decimal_from_z_wires (self) -> int:
        wires = [
            (wire, value)
            for wire, value in self.wires.items()
            if wire.startswith("z")
        ]
        wires.sort(reverse=True)
        return int(
            "".join(str(value) for _, value in wires),
            base = 2
        )

example = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""
puzzle = """"""

assert CrossedWires(example).decimal_from_z_wires() == 2024
print("Part 1:", CrossedWires(puzzle).decimal_from_z_wires())