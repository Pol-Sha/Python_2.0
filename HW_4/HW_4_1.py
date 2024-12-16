#  Напишите функцию для транспонирования матрицы

def transposition_matrix(matrix: list[list])-> list[list]:
    """ Транспонирование матрицы"""
    transpose_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transpose_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transposition_matrix(matrix))


