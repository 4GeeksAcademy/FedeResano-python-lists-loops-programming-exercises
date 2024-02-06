def matrix_builder(num):
    matrix = []

    for i in range(num):
        row = []
        for j in range(num):
            row.append(1)
        matrix.append(row)

    return matrix

print(matrix_builder(3))
