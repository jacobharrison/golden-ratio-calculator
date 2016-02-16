#!/usr/local/bin/python3.5

'''
    Golden Ratio Calculator
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

def get_smaller_phi ( value ) :
    # Find the nearest smaller golden value
    return float(value) / phi

def get_larger_phi ( value ) :
    # Find the nearest larger golden value
    return float(value) * phi

def find_golden ( value ) :
    if not is_number( value ):
        return "\nSorry, %s, is not a number\n\n" % value
    else:
        smaller = round ( get_smaller_phi ( value ), rounder )
        bigger = round ( get_larger_phi ( value ), rounder )
        return ( "\n" + str( bigger ) + " : " + str( value ) + " : " + str( smaller ) + "\n\n" )

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
