from virtual_machine import VirtualMachine
from opcodes import OPCODES


if __name__ == "__main__":
    program = [
        (OPCODES.LOAD << 12) + 0xA,  # Load the value at address 0xA into AC
        (OPCODES.ADD << 12) + 0xB,   # Add the value at address 0xB to AC
        (OPCODES.STORE << 12) + 0xC, # Store the result in address 0xC
        (OPCODES.OUTPUT << 12),      # Output the value in AC
        (OPCODES.HALT << 12)         # Halt the program
    ]

    data = {
        0xA: 0x10,  # 16 in hex
        0xB: 0x5    # 5 in hex
    }

    vm = VirtualMachine()
    vm.load_program(program)

    for address, value in data.items():
        vm._memory[address] = value  # Load data into memory

    vm.run()  # Run the MARIE machine
