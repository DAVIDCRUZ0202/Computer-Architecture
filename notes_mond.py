"""
Number Bases
_________________________________

It's the "language" that a number is written down in

Douze(french) == (english)Twelve
same thing!!

1100(binary) == 12 
same thing!!

base 2: binary
base 8: Octal(rarely used)
base 10: decimal (what we know from grade school)
base 16: hexadecimal "hex"
base 64: base 64

base 10(decimal)




|<----- 1000's place 10^3
||<----- 100's place 10^2
|||<---- 10's place 10^1
||||<---- 1's place 10^0
abcd
1234
1 1000
2 100s
3 10s
4 1s

1234 = 1 * 1000 + 2 * 100 + 3 + 10 + 4 * 1
       ^          ^         ^        ^

"""

"""
For Hex, our digits are represented
by 0-9, and then A-F
and each place value is the next 16th power
"""

"""
Here's a binary conversion

|<----- 8's place 2^3
||<----- 4's place 2^2
|||<---- 2's place 2^1
||||<---- 1's place 2^0
abcd

0011 binary

0011 binary == 0 * 8 + 0 * 4 + 1 * 2 + 1 * 1 == 3 decimal

*** FOR ANY NUMBER BASE, YOU CAN PUT ANY NUMBER OF LEADING 0'S***

binary digits == ("bit")

8 bits == "byte"
4 bits == "nybble"

"""

"""
The number base only matters
when you write the number down.
Once it's inside of a machine, the
number base doesn't matter.
"""

"""
Default languages work in base 10 most of the time.

To specify the base in code:
Prefix
______
[none] decimal
0b  binary
0x  hex
0o  octal

bases only matter when you want to print it out
all numeric values are simply numeric values
written in one language or another

"""

"""
As the base number gets bigger, 
the amount of digits required to represent
a numerical value goes down.
"""

"""
4 bits(One nybble) are(is) required to store
one hex digit.


"""

"""
Converting from binary to hex is very easy!
Nybbles align the digit counting between binary and hexadecimal very well.
When converting, just chop up a binary number into 4's
and then translate!
"""

# Beej's Emulator
# Memory works like a giant array
# Think of your RAM as a massive Array
# In the compyter, we have a RAM which contains memory


# Index into the memory array
# Address
# Location
# Pointer
# The above all mean the same thing!!

memory = [
    # we can put any number we want in here
    # and assign them to mean something
    1, # PRINT_DAVID - Address 0
    3, # SAVE_REG - R1, 37 # Op Code
    1, # SAVE_REG - R1 # Operand
    37,# SAVE_REG - 37 # Operand
    2, # HALT
    # we can hold any number in here but 256
    # because 256 can't be represented in binary
    

    #....... Dynamic Ram has 8 capacitors for bytes.
    #....... meaning that D-Ram can't store anything above 8 bits.


]

register = [0] * 8 # represent r0 - r7
# the below says store the value 37 in register 2


# "Variables" in hardware, known as "registers"
# There are a fixed number of registers
# They have fixed names
# On the LS8, they're called...
# R1 R2 R3 R4 R5 R6 R7


pc = 0# Program Counter, address of the currently-executing instruction

running = True

while running:
    ir = memory[pc] # Instruction Register
    # This holds a copy of the currently executing instruction
    
    if ir == 1:
        print("David")
        pc += 1
    elif ir == 2:
         running = False

    elif ir == 3: # Save Reg
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        register[reg_num] = value
        print(register)
        pc += 3

    elif ir == 4:
        reg_num = memory[pc + 1]
        print(register[reg_num])
        pc += 2
    else:
        print(f"Unknown Instruction {ir}")
         

### The above is a very basic emulation
### Memory has numbers. Those numbers
# have meaning, and we can tell the computer
# what those meanings are.

# Interrupts are a stretch goal