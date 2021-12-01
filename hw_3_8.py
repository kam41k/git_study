matrix = []
for i in range(5):
    row = []
    for j in range(4):
        row.append(int(input(f'Введите число для {i+1} ряда матрицы: ')))
    row.append(sum(row))
    matrix.append(row)
print()
for row in matrix:
    for elem in row:
        print(elem, end=' ')
    print()
