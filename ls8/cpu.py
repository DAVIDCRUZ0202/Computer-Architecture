"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256 # 256 bytes of memory
        self.reg = [0] * 8 # 8 general purpose registers
        self.pc = 0 # Program Counter

    def ram_read(self,MAR): # Memory Address Register
        return self.ram[MAR] # register used for addresses

    def ram_write(self, MDR, MAR): # Memory Data Register
        self.ram[MAR] = MDR # register used for data
        return print(f"Writing {MDR} to {MAR} Complete")

    
    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000, # NOP - Do nothing
            0b00001000, # Binary for 8
            0b01000111, # PRN R0
            0b00000000, # NOP - Do nothing
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        self.IR = self.ram[self.pc] # instruction register
        operand_a = self.ram_read(self.pc+1)
        operand_b = self.ram_read(self.pc+2)

        if self.IR == 0b10000010:
            reg_num = operand_a
            reg_val = operand_b
            self.reg[reg_num] = reg_val
            print(self.reg[reg_num])
            self.pc += 3


        elif self.IR == 0b00000001:
            self.hlt()

        else:
            self.hlt()

    def hlt(self):
        print("Program Ended")



# program = [
#             # From print8.ls8
#          0  0b10000010, # LDI R0,8
#          1  0b00000000, # NOP - Do nothing
#          2  0b00001000, # Binary for 8
#          3  0b01000111, # PRN R0
#          4  0b00000000, # NOP - Do nothing
#          5  0b00000001, # HLT
#         ]

