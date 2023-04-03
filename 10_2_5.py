def matrix_operation(matrix1, matrix2, operation):
    result = []
    n = len(matrix1)
    m = len(matrix1[0])
    for i in range(n):
        row = []
        for j in range(m):
            if operation == '+':
                row.append(matrix1[i][j] + matrix2[i][j])
            elif operation == '-':
                row.append(matrix1[i][j] - matrix2[i][j])
            elif operation == '*':
                row.append(matrix1[i][j] * matrix2[i][j])
        result.append(row)
    return result

# Пример использования функции
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
operation = '+'
result = matrix_operation(matrix1, matrix2, operation)
print("Результат операции над матрицами:", result)
