#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastDigit = (-number) % 10
    lastDigit = -lastDigit
else:
    lastDigit = number % 10

stringToPrint = f"Last digit of {number} is {lastDigit} "

if lastDigit > 5:
    stringToPrint += "and is greater than 5"
elif lastDigit == 0:
    stringToPrint += "and is 0"
else:
    stringToPrint += "and is less than 6 and not 0"

print(stringToPrint)
