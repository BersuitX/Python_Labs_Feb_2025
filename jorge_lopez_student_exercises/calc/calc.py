#! /usr/bin/python
# Author: BersuitX 
# Description: This about script does
"""
    Docstring:
"""

import sys
import basic
import adv

def main():
    menu = """
        Calculator App
        --------------
        1. test basic
        2. test Adv
    """

    print(menu)
    option = input("Choose 1 or 2: ")
    if option == "1":
        print(f"100 + 50 + 25 + 12.5 = {basic.add(100, 50, 25, 12.5)}")
        print(f"100 * 50 * 25 * 12.5 = {basic.mul(100, 50, 25, 12.5)}")
    elif option == "2":
        print(f"Modulus of 100 by 45 = {adv.mod(100, 45)}")
        print(f"Square root of 25 = {adv.sqrt(25)}")
    else:
        print("Invalid options")
    return None

if __name__ == "__main__":
    main()
    sys.exit(0)