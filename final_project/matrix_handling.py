import os
import random


def get_file_path(filename):
    if os.path.isabs(filename):
        return filename
    return os.path.join(os.path.dirname(__file__), filename)


#loads a matrix from a file
def load_matrix(matrix_name):
    matrix = []
    with open(get_file_path(matrix_name), "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            row = [value.strip() for value in line.strip("[]").split(",") if value.strip()]
            if not row:
                continue

            matrix.append([float(value) for value in row])
    return matrix

def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = [0] * cols
        matrix.append(row)
    return matrix

#randomises the entire matrix
def randomise_matrix(matrix):
    #randomises the specified cell, cell is actually just another name of which matrix
    def randomise_cell(cell, x, y):
        cell[x][y] = random.uniform(-0.1, 0.1)
        return cell[x][y]  
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = randomise_cell(matrix, i, j)
    return matrix

#saves the matrix to a file
def save_matrix(matrix, filename):
    with open(get_file_path(filename), "w") as file:
        for row in matrix:
            file.write("[{}]\n".format(", ".join(str(x) for x in row)))


def hadamard_product(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("Matrices must have the same dimensions for Hadamard product.")
    elif len(matrix_a) != len(matrix_b):
        raise ValueError("Matrices must have the same dimensions for Hadamard product.")
    return [
        [a * b for a, b in zip(row_a, row_b)]
        for row_a, row_b in zip(matrix_a, matrix_b)
    ]

def matrix_multiplication(matrix_a, matrix_b):
    result = create_matrix(len(matrix_a), len(matrix_b[0]))
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("Number of columns in matrix A must be equal to number of rows in matrix B.")
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]
    return result