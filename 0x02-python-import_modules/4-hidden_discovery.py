#!/usr/bin/python3

import hidden_4

if __name__ == '__main__':
    for str in dir(hidden_4):
        if len(str) > 2 and str[0:2] != "__":
            print(str)
