#!/usr/bin/python3

""" Contains the matrix_divided function """


def matrix_divided(matrix, div):
    """
    Takes a matrix (list of lists) and divide it by the div number
    """

    strErrorOne = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(strErrorOne)

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if len(matrix) == 0:
        return []

    if not isinstance(matrix[0], list):
        raise TypeError(strErrorOne)

    lenOfMatrix = len(matrix[0])
    newMatrix = []

    for singleList in matrix:
        if not isinstance(singleList, list):
            raise TypeError(strErrorOne)

        if len(singleList) != lenOfMatrix:
            raise TypeError("Each row of the matrix must have the same size")

        newList = []

        for num in singleList:
            if not isinstance(num, int) and not isinstance(div, float):
                raise TypeError(strErrorOne)
            divResult = round(num / div, 2)
            newList.append(divResult)

        newMatrix.append(newList)

    return newMatrix
