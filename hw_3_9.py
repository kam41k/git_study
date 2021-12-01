from random import randint
matrix = []
min_list = []
i = 5  # можно input
j = 5  # для ввода размера матрицы
for k in range(i):
    row = []
    for n in range(j):
        row.append(randint(1,100))
    matrix.append(row)
for row in matrix:
    for elem in row:
        print(f'{elem}'.zfill(2), end=' ')
    print()
for k in range(j):
    min = matrix[0][k]
    for n in range(i):
        if matrix[n][k] < min:
            min = matrix[n][k]
    min_list.append(min)
print()
print(min_list)
print(f'Максимальный элемент среди минимальных элементов столбцов - {max(min_list)}')
