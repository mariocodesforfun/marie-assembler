# marie-assembler
marie-assembler

marie-assembler is a Python-based assembler for the MARIE architecture, which is a simplified architecture often used for educational purposes. This project provides tools to assemble MARIE assembly code into machine code that can be executed by a MARIE virtual machine.

Note: It's recommended to run the code in a virtual environment (venv) to manage dependencies cleanly.

Project Structure
vm logic: virtual_machine.py contains the logic for the MARIE virtual machine, including instruction execution and memory management.
opcodes: opcodes.py defines the opcodes used in MARIE assembly language, mapping them to their binary representations.
Example Programs:
add_example.py demonstrates a simple addition program in MARIE assembly language.
subtraction_example.py showcases a subtraction program.
jump_cond_example.py illustrates the usage of jump and conditional skip instructions in MARIE assembly.
Feel free to explore the provided examples and adapt them for your own projects or educational purposes.


HOW TO RUN THE CODE:
1. Clone the github repository
2. cd marie-assembler
3. setup venv
4. optioanl(only if you do not have main python packages install):
   pip install -r requirements.txt
5. Running Examples:
    a. python add_example.py
    b. python subtraction_example.py
    c. python jump_cond_example.py



