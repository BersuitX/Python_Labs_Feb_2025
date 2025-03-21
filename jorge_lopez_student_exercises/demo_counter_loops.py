#! /usr/bin/python
# Author: BersuitX 
# Description: This about script HOWTO repeat a block of
# commands a specific number of times using a COUNTER loop.
"""
    Docstring:
"""

count = 0 # 1.Init counter
while count < 10: # 2.Test counter
    print(count)
    count += 1 # 4.Increment counter

# Alternatively, we could use a FOR loop plus the built-in
# range(start, stop, step) function. STEP increment is INTEGER!
for num in range(0, 10, 2):
    print(num)

# range(start, stop, step=1) function.
for num in range(0, 10):
    print(num)

# range(start=0, stop, step=1) function.
for num in range(10):
    print(num)