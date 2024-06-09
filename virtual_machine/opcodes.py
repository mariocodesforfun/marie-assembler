from enum import IntEnum

class OPCODES(IntEnum):
    LOAD = 0x1
    STORE = 0x2
    ADD = 0x3
    SUBT = 0x4
    INPUT = 0x5
    OUTPUT = 0x6
    HALT = 0x7
    SKIPCOND = 0x8
    JUMP = 0x9
