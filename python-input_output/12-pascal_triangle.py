#!/usr/bin/python3


def pascal_triangle(n):
    """ Define a function that generates Pascal's triangle up to n rows

    Parameters:
    - n (int): The number of rows of Pascal's triangle to generate

    Returns:
    - list of lists: A list containing n lists, where each inner list represents a row of Pascal's triangle
    """

    # If the input n is less than or equal to 0, return an empty list
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row containing a single 1
    pasc_triangle = [[1]]

    # Generate each row of Pascal's triangle, starting from the second row until the nth row
    for rows in range(n - 1):
        # The first element of each row is always 1
        line = [1]

        # Calculate the values for the middle elements of the row
        # This is done by adding the elements from the previous row
        # For example, to get the middle elements of row 3, we add the elements of row 2 pairwise
        for i in range(rows):
            line.append(pasc_triangle[rows][i] + pasc_triangle[rows][i + 1])

        # The last element of each row is always 1
        line.append(1)

        # Append the constructed row to Pascal's triangle
        pasc_triangle.append(line)

    # Return the completed Pascal's triangle
    return pasc_triangle
