#!/usr/bin/python3

def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    lastChar = 'M'
    number = 0
    if roman_string is None or roman_string is not str:
        return 0
    for char in roman_string:
        currentInt = romans[char]
        lastInt = romans.get(lastChar)
        if currentInt > lastInt:
            number += (currentInt - 2 * lastInt)
        else:
            number += currentInt
        lastChar = char
    return number
