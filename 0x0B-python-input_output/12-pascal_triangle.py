#!/usr/bin/python3
"""
Pascal Triangal problem solution
"""


def pascal_triangle(n):
    """
    A function that takes an integer n, and computes pascal triangal
    """

    result = []

    for i in range(n):
        arr = []
        if i == 0:
            arr.append(1)
        elif i == 1:
            arr.append(1)
            arr.append(1)
        else:
            arr.append(1)
            for j in range(len(result[i - 1]) - 1):
                arr.append(result[i - 1][j] + result[i - 1][j + 1])
            arr.append(1)
        result.append(arr)
    return result
