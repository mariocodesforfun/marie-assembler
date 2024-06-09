from virtual_machine import VirtualMachine
from opcodes import OPCODES

if __name__ == "__main__":
    program = [
        # Load operations
        (OPCODES.LOAD << 12) + 0xA,  # Load the value at address 0xA into AC
        (OPCODES.LOAD << 12) + 0xB,  # Load the value at address 0xB into AC
        # Conditional check
        (OPCODES.SKIPCOND << 12) + 0x0,  # Skip if AC < 0
        (OPCODES.JUMP << 12) + 0x6,  # Jump to address 0x6 if AC < 0
        # Addition
        (OPCODES.ADD << 12) + 0xB,   # Add the value at address 0xB to AC
        # Output operation
        (OPCODES.OUTPUT << 12),      # Output the value in AC
        # Halt operation
        (OPCODES.HALT << 12)         # Halt the program
    ]

    # Data to be loaded into memory
    data = {
        0xA: 0x10,  # Value for the first operand
        0xB: 0x5,   # Value for the second operand
    }

    # Initialize Virtual Machine and load program
    vm = VirtualMachine()
    vm.load_program(program)

    # Load data into memory
    for address, value in data.items():
        vm._memory[address] = value

    # Run the MARIE machine
    vm.run()
