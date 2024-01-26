#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if ord(char) <= ord('z') and ord(char) >= ord('a'):
            char = chr(ord(char) - ord('a') + ord('A'))
        print('{}'.format(char), end='')
    print()
