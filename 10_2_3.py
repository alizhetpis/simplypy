def rotate_matrix(matrix):
    # Используем функции zip(), list() и reversed() для поворота матрицы
    return [list(reversed(column)) for column in zip(*matrix)]

# Пример использования функции
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated_matrix = rotate_matrix(matrix)
print(rotated_matrix)
