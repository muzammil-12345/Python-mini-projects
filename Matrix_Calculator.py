'''
 Day 29: Matrix Calcuator Using Numpy
 Topics Covered:
 1. Introduction to Numpy
 2. Matrix Operations using Numpy
 3. Handling User Inputs for matrices
 4. Building a matrix calcuator
 5. Project: Matrix Calcuator
'''

# What is Numpy/
'''
Numpy or Numerical Python is a foundational library in python
for numerical competitions. It provides a fast, efficient way
to perform operations on datasets using arrays and supports
advance mathematical functions.
'''
# import numpy as np
# # Creating a 2x2 matrix using numpy
# matrix = np.array([[1, 2], [3, 4]])
# print("Matrix:\n", matrix)

# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])

# # Matrix Operations using Numpy

# # Adding two matrices
# print("Addition of two matrices:\n", a + b)

# # Subtracting two matrices
# print("Subtraction of two matrices:\n", a - b)

# # Multiplying two matrices
# print("Element-wise Multiplication of two matrices:\n", a * b)

# # Dot product of two matrices
# print("Dot Product of two matrices:\n", np.dot(a, b))

# # Transpose of a matrix
# print("Transpose of a matrix:\n", a.T) # Or we can try "np.transpose(a)"

# # Determinant of a matrix
# det_a = np.linalg.det(a) # fucntion for calculating determinant of a matrix is "np.linalg.det()"
# print("Determinant of matrix a:", det_a)

# # Inverse of a matrix
# if det_a != 0:
#     inv_a = np.linalg.inv(a) # function for calculating inverse of a matrix is "np.linalg.inv()"
#     print("Inverse of matrix a:\n", inv_a)


# # Handling user inputs for matrices
# # Function to Create matrix from user input
# def get_matrix():
#     rows = int(input("Enter the number of rows: "))
#     cols = int(input("Enter the number of columns: "))
#     print("Enter the elements of the matrix row by row:")
#     elements = []
#     for _ in range(rows):
#         row = list(map(float, input().split()))
#         elements.append(row)
#     return np.array(elements)

# matrix1 = get_matrix()
# print("Matrix 1:\n", matrix1)

# --- Project: Matrix Calculator ---

import numpy as np

def get_matrix():
    try:
        rows = int(input("Enter the number of rows for the matrices: "))
        cols = int(input("Enter the number of columns for the matrices: "))
        print("Enter the elements of the first matrix row by row:")
        elements = []
        for _ in range(rows):
            row = list(map(float, input().split()))
            if len(row) != cols:
                raise ValueError("Numbers of elements in the row do not match the specified number of columns.")
            elements.append(row)
        return np.array(elements)
    except ValueError as e:
        print("Error:", e)
        return None

# Matrix Operations
def matrix_operations(a, b):
    print("Matrix 1:\n", a)
    print("Matrix 2:\n", b)

    # Addition
    try:
        print("Addition of two matrices:\n", a + b)
    except ValueError:
        print("Addition not possible due to shape mismatch.")    

    # Subtraction
    try :
        print("Subtraction of two matrices:\n", a - b)
    except ValueError:
        print("Subtraction not possible due to shape mismatch.")

    # Element-wise Multiplication
    try:
        print("Element-wise Multiplication of two matrices:\n", a * b)
    except ValueError:
        print("Element-wise multiplication not possible due to shape mismatch.")

    # Dot Product
    try:
        print("Dot Product of two matrices:\n", np.dot(a, b ))
    except ValueError:
        print("Number of columns in the first matrix must match the number of rows in the second matrix for dot product.")

    # Transpose
    print("Transpose of Matrix 1:\n", a.T)
    print("Transpose of Matrix 2:\n", b.T)

    # Determinant
    try:
        print("Determinant of Matrix 1:", np.linalg.det(a))
    except np.linalg.LinAlgError:
        print("Determinant of a: Not applicable (Matrix must be square matrix).")

    # Inverse 
    try:
        print("Inverse of Matrix 1:\n", np.linalg.inv(a))
    except np.linalg.LinAlgError:
        print("Inverse of a: Not applicable (Matrix must be square and non-singular).")

# Main program
def main():
    print("============================")
    print(" --- Matrix Calculator ---")
    print("============================")
    print("Enter the first matrix:")
    a = get_matrix()
    if a is None:
        return
    print("Enter the second matrix:")
    b = get_matrix()
    if b is None:
        return

    matrix_operations(a, b)

if __name__ == "__main__":
    main()    
