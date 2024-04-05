#!/usr/bin/python3
"""Define a function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    # Check if m_a and m_b are lists --> if not, raise a TypeError
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')

    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    # Check if m_a and m_b are lists of lists --> if not, raise a TypeError
    for row in m_a:
        if type(row) is not list:
            raise TypeError('m_a must be a list of lists')

    for row in m_b:
        if type(row) is not list:
            raise TypeError('m_b must be a list of lists')

    # Check if m_a and m_b are empty --> if yes, raise a ValueError
    if len(m_a) is 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) is 0:
        raise ValueError("m_b can't be empty")

    # Check if any row in m_a or m_b is empty --> if yes, raise a ValueError
    for row in m_a:
        if len(row) is 0:
            raise ValueError("m_a can't be empty")

    for row in m_b:
        if len(row) is 0:
            raise ValueError("m_b can't be empty")

    # Check if all elements in m_a and m_b are integers or floats --> if not, raise a TypeError
    for row in m_a:
        for value in row:
            if type(value) is not int and type(value) is not float:
                raise TypeError('m_a should contain only integers or floats')

    for row in m_b:
        for value in row:
            if type(value) is not int and type(value) is not float:
                raise TypeError('m_b should contain only integers or floats')

    # Check if all rows in m_a and m_b have the same size --> if not, raise a TypeError
    row_len = len(m_a[0])

    for row in m_a:
        if len(row) is not row_len:
            raise TypeError('each row of m_a must be of the same size')

    row_len = len(m_b[0])

    for row in m_b:
        if len(row) is not row_len:
            raise TypeError('each row of m_b must be of the same size')

    # Check if the number of columns in m_a equals the number of rows in m_b for matrix multiplication
    # If not, raise a ValueError
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    new_matrix = []  # Initialize the result matrix

    for a_row in range(len(m_a)):
        new_row = []  # Initialize a new row for the result matrix
        # m_a width must equal m_b height

        for b_col in range(len(m_b[0])):
            sum = 0  # Initialize sum for the dot product

            for a_col in range(len(m_a[0])):
                # Multiply corresponding elements and add to the sum
                prod = m_a[a_row][a_col] * m_b[a_col][b_col]
                sum += prod

            new_row.append(sum)  # Append the sum to the new row

        new_matrix.append(new_row)  # Append the new row to the result matrix

    return new_matrix  # Return the result matrix
