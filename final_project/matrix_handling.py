import random

#loads a matrix from a file
def load_matrix(mart_name):
    matrix = []
    with open(mart_name, "r") as file:
        for line in file:
            row=(line.strip()).replace("[", "").replace("]", "").replace(", ", ",")
            matrix.append(row.split(","))
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

#saves the matrix to a file
def save_matrix(matrix, filename):
    with open(filename, "w") as file:
        for row in matrix:
            file.write("[{}]\n".format(", ".join(str(x) for x in row)))


matrix = load_matrix("input_handling_matr.txt")

randomise_matrix(matrix)

save_matrix(matrix, "output_matrix.txt")