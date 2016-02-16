#!/usr/bin/env python3

'''
    Goldie, a golden ratio calculator
    Written by Jacob Harrison
    JH@JHarrison.co
'''

import sys
import math

# Variables
args = sys.argv
phi = ( 1 + math.sqrt(5) ) / 2

# Program Options
steps = 3
rounder = 2

def stringify ( s, v, l ) :

    # Formats the output into a readable string
    # YELLOW = '\033[93m'
    # BOLD = '\033[1m'
    # END = '\033[0m'

    result = "\n\n\033[93m\033[1m" + "Golden Numbers" + "\033[0m\033[0m\n"

    # Loops through the larger
    for i, e in reversed ( list ( enumerate ( l ) ) ) :
        if i == 0:
            # result += "\n"
            continue

        step_up = round ( float ( l[i] ), rounder )
        result += str ( step_up )

        if i != 1 :
            result += ", "
        else:
            result +=", \033[93m\033[1m"

    result += v

    for i, e in enumerate ( s, start=1 ) :
        if i == 1:
            result += "\033[0m\033[0m, "
            continue

        step_down = round ( float ( s[i-1] ), rounder )
        result += str ( step_down )

        if len(s) != i :
            result += ", "
        else:
            result += "\n\n"
    # result += str ( round ( l, rounder ) ) + " : "
    # result += str ( v ) + " : "
    # result += str ( round ( s, rounder ) ) + "\n\n"
    return result

def get_smaller_phi ( value ) :
    # Find the nearest smaller golden value
    smaller = [value]
    for i in range(1, steps + 1):
        smaller.append ( float ( smaller[i-1] ) / phi )

    return smaller

def get_larger_phi ( value ) :
    # Find the nearest larger golden value
    larger = [value]
    for i in range( 1, steps + 1 ):
        larger.append ( float ( larger[i-1] ) * phi )

    return larger

def is_number ( s ) :
    # Checks if argument is a number
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False

def find_golden ( value ) :
    if not is_number( value ):
        return "\nSorry, %s, is not a number\n\n" % value
    else:
        smaller = get_smaller_phi ( value )
        bigger = get_larger_phi ( value )
        return ( stringify( smaller, value, bigger ) )

def main () :
    # Make sure we've got the corrent input
    if len(args) >= 3 :
        print ( "\nI'm sorry, you've entered too many parameters\n\n" )
    elif len(args) <= 1:
        # If the user provides no arguments, ask them for a number
        value = input("\nPlease enter a number: ")
        while not is_number( value ):
            value = input("\nNo, a number: ")
            if is_number( value ):
                break
        print ( find_golden( value ) )
    else:
        print ( find_golden( args[1] ) )

if __name__ == "__main__":
    main()
