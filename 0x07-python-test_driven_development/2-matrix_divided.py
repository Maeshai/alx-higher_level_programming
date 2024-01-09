def matrix_divided(matrix, divisor):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        divisor (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numeric elements.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If divisor is not an int or float.
        ZeroDivisionError: If divisor is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    if (not isinstance(matrix, list) or not matrix or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, (int, float)))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(divisor, (int, float)):
        raise TypeError("divisor must be a number")

    if divisor == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / divisor, 2), row)) for row in matrix]
