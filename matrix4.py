import numpy as np

# input the number of rows and columns of the matrix
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# input the elements of the matrix
print("Enter the elements of the matrix:")
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
        matrix.append(row)

# convert the matrix to numpy array
matrix = np.array(matrix)

# find transpose of the matrix
transpose = np.transpose(matrix)

# print the original matrix and its transpose
print("Original Matrix:")
print(matrix)
print("Transpose of the matrix:")
print(transpose)

# check if the matrix is symmetric
is_symmetric = np.allclose(matrix, transpose)

if is_symmetric:
    print("The matrix is symmetric")
else:
    print("The matrix is not symmetric")
