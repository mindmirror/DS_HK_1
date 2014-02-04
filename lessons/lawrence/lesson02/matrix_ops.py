"""
Lession 2 classwork

Write two functions: matrixVector multiplication and matrix multiplication.
"""

vector1 = [1, 2, 3]
vector2 = [1, 2]
matrix1 = [[1, 2, 3],
           [4, 5, 6]]
matrix2 = [[1, 2, 3],
           [4, 5]]
matrix3 = [[1, 2],
           [3, 4],
           [5, 6]]

def isValidMatrix(matrix):
    for row in matrix:
        if not isinstance(row, list) or len(row) != len(matrix[0]):
            return False
    return True

def matrixVectorMul(matrix, vector):
    """
    Check the matrix is valid
    """
    if  not isValidMatrix(matrix):
        raise Exception("Invalid matrix")

    """
    Check the number of column in matrix is equal to the lenth of vector
    """
    if not len(matrix[0]) == len(vector):
        raise Exception("The number of columns in matrix is not equal to the lenth of vector")

    r = []
    for row in matrix:
        sum = 0
        for i in range(len(vector)):
            sum += row[i] * vector[i]
        r.append(sum)
    return r

# Invalid matrix
#print matrixVectorMul(matrix2, vector1)

# The number of matrix columns is not equal to the lenth of vector
#print matrixVectorMul(matrix1, vector2)

# Correct matrix vector multiplication
print matrixVectorMul(matrix1, vector1)


def matrixMul(mat1, mat2):
    if not isValidMatrix(mat1) or not isValidMatrix(mat2):
        raise Exception("Invalid matrix")

    if not len(mat1[0]) == len(mat2):
        raise Exception("The number of matrix1 columns is not equal to the number of matrix2 rows")

    r = []
    for i in range(len(mat1)):
        new_row = []
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat1[0])):
                sum += mat1[i][k] * mat2[k][j]
            new_row.append(sum)
        r.append(new_row)
    return r

print matrixMul(matrix1, matrix3)


def iMatrix(n):
    if not isinstance(n, int):
        raise Exception("Dimension n is not a integer")

    return [[1 if j == i else 0 for i in range(n)] for j in range(n)]

print iMatrix(4)
