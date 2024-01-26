#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if number < 0:
    lastDigit = -lastDigit

stringToPrint = f"Last digit of {number} is {lastDigit} "

if lastDigit > 5:
    stringToPrint += "and is greater than 5"
elif lastDigit == 0:
    stringToPrint += "and is 0"
else:
    stringToPrint += "and is less than 6 and not 0"

print(stringToPrint)
