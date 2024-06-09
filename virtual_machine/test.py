import unittest
from virtual_machine import VirtualMachine
from opcodes import OPCODES
from typing import List

class TestVirtualMachine(unittest.TestCase):

    def setUp(self):
        self.vm = VirtualMachine()

    def load_and_run(self, program: List[int], data: dict):
        self.vm.load_program(program)
        for address, value in data.items():
            self.vm._memory[address] = value
        self.vm.run()

    def test_load(self):
        program = [(OPCODES.LOAD << 12) + 0xA, (OPCODES.OUTPUT << 12), (OPCODES.HALT << 12)]
        data = {0xA: 0x14}
        self.load_and_run(program, data)

    def test_add(self):
        program = [
            (OPCODES.LOAD << 12) + 0xA,
            (OPCODES.ADD << 12) + 0xB,
            (OPCODES.OUTPUT << 12),
            (OPCODES.HALT << 12)
        ]
        data = {0xA: 0x10, 0xB: 0x05}
        self.load_and_run(program, data)

    def test_subtract(self):
        program = [
            (OPCODES.LOAD << 12) + 0xA,
            (OPCODES.SUBT << 12) + 0xB,
            (OPCODES.OUTPUT << 12),
            (OPCODES.HALT << 12)
        ]
        data = {0xA: 0x10, 0xB: 0x05}
        self.load_and_run(program, data)

    def test_store(self):
        program = [
            (OPCODES.LOAD << 12) + 0xA,
            (OPCODES.STORE << 12) + 0xB,
            (OPCODES.OUTPUT << 12),
            (OPCODES.HALT << 12)
        ]
        data = {0xA: 0x10}
        self.load_and_run(program, data)

    def test_jump(self):
        program = [
            (OPCODES.LOAD << 12) + 0xA,
            (OPCODES.JUMP << 12) + 0x4,
            (OPCODES.HALT << 12),
            (OPCODES.OUTPUT << 12)
        ]
        data = {0xA: 0x10}
        self.load_and_run(program, data)

    def test_halt(self):
        program = [(OPCODES.HALT << 12)]
        self.load_and_run(program, {})

    def test_invalid_opcode(self):
        program = [0xF000]  # Invalid opcode
        self.load_and_run(program, {})

if __name__ == "__main__":
    unittest.main()
