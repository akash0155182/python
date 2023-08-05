import numpy as np

matrix1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
matrix2 = np.array([[4, 3, 2, 1], [8, 7, 6, 5], [12, 11, 10, 9]])

# Element-wise sum
sum = matrix1 + matrix2
print("Element-wise sum of the two matrices:")
print(sum)

# Element-wise difference
difference = matrix1 - matrix2
print("\nElement-wise difference of the two matrices:")
print(difference)

# Element-wise product
product = matrix1 * matrix2
print("\nElement-wise product of the two matrices:")
print(product)

# Element-wise quotient
quotient = matrix1 / matrix2
print("\nElement-wise quotient of the two matrices:")
print(quotient)
