#!/usr/local/bin/python3.5

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
    result = "\n"
    result += str ( round ( l, rounder ) ) + " : "
    result += str ( v ) + " : "
    result += str ( round ( s, rounder ) ) + "\n\n"
    return result

def get_smaller_phi ( value ) :
    # Find the nearest smaller golden value
    return float(value) / phi

def get_larger_phi ( value ) :
    # Find the nearest larger golden value
    return float(value) * phi

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
