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


For Hexadecimal, our digits are represented
by 0-9, and then A-F
and each place value is the next 16th power

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

One byte is the most common standard unit of memory used for our CPU

4 bits == "nybble"

The number base only matters
when you write the number down.
Once it's inside of a machine, the
number base doesn't matter.

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

As the base number gets bigger, 
the amount of digits required to represent
a numerical value goes down.

4 bits(One nybble) are(is) required to store
one hex digit.


Converting from binary to hex is very easy!
Nybbles align the digit counting between binary and hexadecimal very well.
When converting, just chop up a binary number into 4's
and then translate!
"""

# Beej's Emulator
# Memory works like a giant array
# Think of your RAM as a massive Array
# In the computer, we have a RAM which contains memory


# Index into the memory array
# Address
# Location
# Pointer
# The above all mean the same thing!!

# For Tonight's assignment, do this in base 2 instead of base 10
# The above code prints all lines of a given file
# it'll print line by line, but we still need to make sure
# to avoid all whitespace
# avoid all comments
# avoid all blank lines
# print out errors for non-commands

memory = [0] * 256

# This is a "Data Driven" program.
# We have to pass in a file to this program in order to get output

import sys

if len(sys.argv) !=2:
    print("usage: comp.py filename")
    sys.exit(1)

try:
    address = 0

    with open(sys.argv[1]) as f:
        for line in f:
            t = line.split('#')
            n = t[0].strip()

            try:

                n = int(n)
            except ValueError:
                print(f"Invalid Number {n}")
                sys.exit(1)
            if n == '':
                continue

            print(repr(n))
            memory[address] = n
            address += 1

except FileNotFoundError:
    print(f"File not found: {sys.argv[1]}")
    sys.exit()

register = [0] * 8 # represent r0 - r7

# "Variables" in hardware, known as "registers"
# There are a fixed number of registers
# They have fixed names
# On the LS8, they're called...
# R1 R2 R3 R4 R5 R6 R7


pc = 0# Program Counter, address of the currently-executing instruction
# Give the register for the stack pointer a symbolic name
# So that developers know where it is
SP = 7
register[SP] = 0xF4

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

    elif ir == 4: # Print_reg
        reg_num = memory[pc + 1]
        print(register[reg_num])
        pc += 2

    elif ir == 5: # PUSH
        # Decrement SP
        register[SP] -= 1

        # Get the reg num to push
        reg_num = memory[pc + 1]

        # Get the value to push
        value = register[reg_num]

        # copy the value to the SP address
        top_of_stack_addr = register[SP]
        memory[top_of_stack_addr] = value

        print(memory[0xea:0xf4])

        pc += 2

    elif ir == 6: # POP
        # Get the reg to pop into
        reg_num = memory[pc + 1]

        # Get the top of stack addr
        top_of_stack_addr = register[SP]

        # Get the value of the top of stack
        value = memory[top_of_stack_addr]

        #Store the value in the register
        register[reg_num] = value

        # Increment SP
        register[SP] += 1

        pc += 2

        print(memory[0xea:0xf4])

    else:
        print(f"Unknown Instruction {ir}")



#_________________________________________________
#  Instruction     location
#   "POP          register"
# copy the value from the address pointed to by the stack pointer,
# put it at the given register
# increment the SP(Stack works Top-Down)
#_____________________________________________
# Instruction   location
# "PUSH         register"
# Decrement the stack pointer
# place the value at the given register
# Stack pointer points at the item most recently pushed
# 


### The above is a very basic emulation
### Memory has numbers. Those numbers
# have meaning, and we can tell the computer
# what those meanings are.

# Interrupts are a stretch goal


#______________________________________________________________
# Frame the Plan from Inputs to Outputs
# Parsing, Normalize, Sanitize
# all mean the same thing
# Take the data, and make it into the same format


#____________________________________________________________
# CPU Stack notes

# These are just like the stack data structure we know

# Push and Pop are standard

# Stack data is stored in RAM

# The "Stack Pointer" keeps track of the address of the top of the stack.

# Typically the stackgrows down from the higher memory addresses

#__________________________
# A Minimal Stack

# A stack needs somewhere to store data: RAM in this case

# A stack needs to keep track of where the top of the stack is: stack pointer

# A Stack needs functionality to push and pop, like always. Push and pop instructions

# In order to store something(PUSH)
# We first decrement the stack pointer
# then push the value onto the memory address which the stack pointer is pointing at
# Decrement stack pointer -> push value to that address

# In order to remove something(POP)
# We POP it into a Register
# POP the value at the stack pointer and copy it into Register
# Increment the stack pointer
# First, copy the value, POP it onto the register. Then Increment the SP
# This doesn't remove values from the stack, but it copies them to a register
# When we push onto the stack, it overrwrites values

# The stack is typically used to store variables
# Also used to return addresses from a subroutine
# Storage of registers and CPU state while handling an interrupt
# Allocation of local variables for a subroutine

# If you PUSH too many items on the stack, you'll begin to 
# overwrite values 

# If you POP from an empty stack, you'll copy NONE onto a register

# Check if a stack is empty by trying to POP from it

# What information must be saved on the stack when the CPU is servicing
# an interrupt? Why? The current state of the processor, and all of it's
# counters, registers, and flags. This is all saved so that it can
# handle the interruption and then pick back up where it left off


#________________________________________________________________
# CPU Interrupts

# Interrupts are commonly generated by peripherals(keyboard, mouse)
# who need to alert the CPU that some work needs to be done.

# When an interrupt occurs, the current state of the processor is saved
# on the stack, and execution continues at the address of the interrupt handler.

# Most CPU's have a lookup table: Interrupt Vector Table.
# This is an array of interrupts to tell the PC how to handle each one.
# It's an array of pointers to handlers, one per interrupt.
# Different CPU's keep the table in different areas of RAM

#______________________________________________________
# Beej's notes

# Stacks are ALWAYS USED for CPU's

# Stack is good for:

# Temporarily storing values
# Making subroutines possible
# Implementing local variables


# It's easy to implement in the CPU hardware


# Conditionals are what we're missing from our emulator

# How does the stack work?

# Low level Stack concept will be used. Boil the stack down
# to it's purest essence. In the case of a CPU, we just need
# to be able to push and pop. memory and location is handled by RAM.
# The stack pointer points to the top of the stack.
# The stack pointer is a general purpose register

# Stacks start from TOP-DOWN
# if it's empty, it always points to the top(f4)
#_________________________________________________
#  Instruction     location
#   "POP          register"
# copy the value from the address pointed to by the stack pointer,
# put it at the given register
# increment the SP(Stack works Top-Down)
#_____________________________________________
# Instruction   location
# "PUSH         register"
# Decrement the stack pointer
# place the value at the given register
# Stack pointer points at the item most recently pushed
#