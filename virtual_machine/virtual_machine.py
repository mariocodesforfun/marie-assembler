import logging

from typing import List

from opcodes import OPCODES


logging.basicConfig(level=logging.INFO)

class VirtualMachine:
    def __init__(self, memory_size: int = 0x1000):
        self._memory_size = memory_size
        self._memory = [0] * self._memory_size  # Memory array
        self._ac = 0  # Accumulator
        self._pc = 0  # Program Counter
        self._ir = 0  # Instruction Register
        self._running = False  # CPU running state

    def load_program(self, program: List[int]) -> None:
        for i, instruction in enumerate(program):
            self._memory[i] = instruction

    def _fetch(self) -> None:
        self._ir = self._memory[self._pc]
        self._pc += 1

    def _execute(self) -> None:
        opcode = self._ir >> 12  # Equivalent to IR // 0x1000
        operand = self._ir & 0xFFF  # Equivalent to IR % 0x1000

        if opcode == OPCODES.LOAD:
            self._ac = self._memory[operand]
        elif opcode == OPCODES.STORE:
            self._memory[operand] = self._ac
        elif opcode == OPCODES.ADD:
            self._ac += self._memory[operand]
        elif opcode == OPCODES.SUBT:
            self._ac -= self._memory[operand]
        elif opcode == OPCODES.INPUT:
            self._ac = int(input("Input a value (hex): "), 16)
        elif opcode == OPCODES.OUTPUT:
            logging.info(f"Output: {hex(self._ac)}")
        elif opcode == OPCODES.HALT:
            self._running = False
        elif opcode == OPCODES.SKIPCOND:
            if (operand == 0x0 and self._ac < 0) or (operand == 0x190 and self._ac == 0) or (operand == 0x320 and self._ac > 0):
                self._pc += 1
        elif opcode == OPCODES.JUMP:
            self._pc = operand
        else:
            logging.error("Invalid opcode")
            self._running = False

    def run(self) -> None:
        self._running = True
        while self._running:
            self._fetch()
            logging.info(f"Executing instruction: {hex(self._ir)}")
            self._execute()
