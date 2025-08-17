# 2D list (matrix) example
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Full Matrix:")
for row in matrix:
    print(row)

print("\nDiagonal Elements:")
for i in range(len(matrix)):
    print(matrix[i][i])