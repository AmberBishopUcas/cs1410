# Shared matrix utilities used by the language model project.
# This file centralizes the data format used by the network, embedding tables,
# and training code so mathematical operations stay consistent across modules.
import os
import random


def get_file_path(filename):
    """Return an absolute path for project files, whether a relative or absolute path is given."""
    if os.path.isabs(filename):
        return filename
    return os.path.join(os.path.dirname(__file__), filename)


def load_matrix(matrix_name):
    """Load a matrix saved as rows like [1, 2, 3] from a text file."""
    matrix = []
    with open(get_file_path(matrix_name), "r") as file:
        for line in file:
            line = line.strip()  # remove trailing whitespace from each saved row
            if not line:
                continue  # skip blank lines in the saved matrix file

            # split the string into values between the brackets and commas
            row = [value.strip() for value in line.strip("[]").split(",") if value.strip()]
            if not row:
                continue  # ignore any empty row that was accidentally saved

            # convert each stored value into a float so the matrix can be used mathematically
            matrix.append([float(value) for value in row])
    return matrix


def create_matrix(rows, cols):
    """Create a 2D matrix filled with zeros of the requested size."""
    matrix = []
    for i in range(rows):
        row = [0] * cols  # each row starts as a zero-filled list
        matrix.append(row)
    return matrix


def randomise_matrix(matrix):
    """Randomize every value in a matrix using a small positive range."""
    def randomise_cell(cell, x, y):
        # fill this one cell with a tiny random value so weights don't start too large
        cell[x][y] = random.uniform(0, 0.2)
        return cell[x][y]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = randomise_cell(matrix, i, j)
    return matrix


def save_matrix(matrix, filename):
    """Write a matrix to disk using one row per line."""
    with open(get_file_path(filename), "w") as file:
        for row in matrix:
            # write each row as a readable list, one row per line in the file
            file.write("[{}]\n".format(", ".join(str(x) for x in row)))


def hadamard_product(matrix_a, matrix_b):
    """Element-wise multiply two matrices of identical shapes."""
    if len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions for Hadamard product.")
    elif len(matrix_a) != len(matrix_b):
        raise ValueError("Matrices must have the same dimensions for Hadamard product.")
    # multiply matching positions in both matrices instead of doing normal matrix multiplication
    return [
        [a * b for a, b in zip(row_a, row_b)]
        for row_a, row_b in zip(matrix_a, matrix_b)
    ]


def matrix_multiplication(matrix_a, matrix_b):
    """Multiply two matrices using the standard row-by-column formula."""
    result = create_matrix(len(matrix_a), len(matrix_b[0]))
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in matrix A must be equal to number of rows in matrix B.")
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                # sum the products for one output cell in the result matrix
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result


def matrix_transpose(matrix):
    """Flip rows and columns so the new matrix uses the old columns as rows."""
    rows = len(matrix)
    collumns = len(matrix[0])
    rc_matrix = create_matrix(collumns, rows)
    for i in range(collumns):
        for j in range(rows):
            # copy each value into its transposed position
            rc_matrix[i][j] = matrix[j][i]
    return rc_matrix


def matrix_print(matrix):
    """Display a matrix in a simple row-by-row format for debugging."""
    for i in range(len(matrix)):
        print(matrix[i])


def get_g(network, layer):
    """Return a derivative-style activation mask for a layer, used by training logic."""
    g = create_matrix(1, len(network[layer]))
    for i in range(len(network)):
        if network[i][0] != 0:
            # mark this neuron as active when it has a nonzero current value
            g[i] = 1
    return g

