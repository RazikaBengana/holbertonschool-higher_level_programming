#!/usr/bin/python3
"""Define a function to divide each element of a matrix by a divisor"""


def matrix_divided(matrix, div):
    # Check if matrix is empty
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each element in the matrix is a list, ensuring it's a matrix of lists
    if all(isinstance(elements, list) for elements in matrix) is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if the first row of the matrix is empty
    if len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows in the matrix are of the same length
    length = len(matrix[0])

    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")

        # Check if each element in the row is an integer or float
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if divisor is a number (either int or float)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    # Check for division by zero error
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the division and round the result to 2 decimal places
    return list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
