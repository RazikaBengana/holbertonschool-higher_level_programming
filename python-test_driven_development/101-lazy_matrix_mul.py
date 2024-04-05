#!/usr/bin/python3
"""Define a function that multiplies 2 matrices by using the module NumPy"""

import numpy


def lazy_matrix_mul(m_a, m_b):

    # Initialize flags to check for various conditions

    m_a_empty = False  # To check if m_a is empty
    m_b_empty = False  # To check if m_b is empty
    m_a_notrect = False  # To check if m_a is not rectangular
    m_b_notrect = False  # To check if m_b is not rectangular
    m_a_notnum = False  # To check if m_a contains non-numeric values
    m_b_notnum = False  # To check if m_b contains non-numeric values
    m_a_scalar = False  # To check if m_a is a scalar (not allowed)
    m_b_scalar = False  # To check if m_b is a scalar (not allowed)

    # Check conditions for matrix m_a
    for row in m_a:
        if not isinstance(row, list):  # Check if any row is not a list, indicating a scalar
            m_a_scalar = True

        if len(row) != len(m_a[0]):  # Check if all rows are of the same length (rectangular matrix)
            m_a_notrect = True

        for num in row:  # Iterate through each element in a row
            if not isinstance(num, (int, float)):  # Check if any element is not an int or float
                m_a_notnum = True

    # Check conditions for matrix m_b similar to m_a
    for row in m_b:
        if not isinstance(row, list):
            m_b_scalar = True

        if len(row) != len(m_b[0]):
            m_b_notrect = True

        for num in row:
            if not isinstance(num, (int, float)):
                m_b_notnum = True

    # Raise errors if any conditions are violated
    if m_a_scalar:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if m_b_scalar:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

    if m_a_notnum:
        raise TypeError("invalid data type for einsum")

    if m_b_notnum:
        raise TypeError("invalid data type for einsum")

    if m_a_notrect:
        raise ValueError("setting an array element with a sequence.")

    if m_b_notrect:
        raise ValueError("setting an array element with a sequence.")

    # Multiply the matrices using NumPy and return the result
    return numpy.matrix(m_a) * numpy.matrix(m_b)
