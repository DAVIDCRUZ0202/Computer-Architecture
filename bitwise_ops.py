# What are bitwise operations?

# They are like boolean operations
# IF, AND , OR , NOT

# These can be used on numeric sets!!
# we can use If, and, etc. on numeric sets
# we can also use XOR , NOR, NAND

# Apply bitwise operations to multibit numbers

# TRUTH Table for "NOT"

# A    Not A
# 0      1
# 1      0

# The above is considered an inverter. NOT is '~' 
# it turns things which are true, into a false and vice versa

# AND, OR

# A    B    A AND B
# 0    0       0
# 0    1       0
# 1    0       0
# 1    1       1

# A    B    A OR B
# 0    0       0
# 0    1       1
# 1    0       1
# 1    1       1


# AND is represented with '&'(ampersand) for bitwise.

# OR is represented with '|'(pipe) for bitwise.

# NAND, NOR

# NAND is inverted version of AND.
# This is done by doing an AND , put it in brackets, and invert it.
# ~(A & B) = NAND statement

# A    B    A NAND B
# 0    0       1
# 0    1       1
# 1    0       1
# 1    1       0

# NOR is inverted version of OR.
# This is done by doing an OR, put it in brackets, and invert it.
# ~(A | B) = NOR statement

# A    B    A NOR B
# 0    0       1
# 0    1       0
# 1    0       0
# 1    1       0

# XOR is exclusive OR.
# This is an OR statement when only one or the other is true, not both.
# XOR is represented with '^'
# Long way of XOR would be
# "A and not-B"
#           OR
#              "Not-A and B"
#                            Not "A and Not-B AND Not-A and B"                            
#   (A & ~B) |    (~A & B) ~((A & ~B) & (~A & B))
#     A ^ B
# A    B    A XOR B
# 0    0       0
# 0    1       1
# 1    0       1
# 1    1       0

# We can use these bitwise operations on multi-bit numbers
# for and statements, pretend you're adding the truth values of each value
#   11101011
# & ++++++++
#   10011101
# ______________
#   10001001


# Example with XOR

#   11011010
# ^ ^^^^^^^^
#   11000011
#_____________
#   00011001

# The AND operator has an interesting property
# The and can be used as a mask

#   11101011
# &
#   11110000
# ______________
# Using the and operator is essentially going to mask values
# any value masked with '1' gets preserved, any value masked
# with '0' gets masked into a 0.

# Shifting is also possible.
# We can shift multibit numbers left and right
# Shift left<<    >>Shift Right

#           1111
#   <<1    11110
# Left shift adds a 0 to the end


#           1111
#   >>1      111
# Right shift removes the last value into nothingness

#   11011111
#~| 
#   00010111
#________________
#   00100000

# A    B    A NOR B
# 0    0       1
# 0    1       0
# 1    0       0
# 1    1       0

#   10101010
#^
#   11110000
#_______________
#   01011010

#   11011
#&
#     101
#____________
#   00001


# Bitwise operations work 1 bit at a time in a number

# in order to compute anything at all, you only need
# one operation

# In General:
# OR can be used to set bits to 1
# AND can be used to set bits to 0



