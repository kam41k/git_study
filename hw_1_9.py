a = int(input('Введите первое число: '))
b = int(input('Введите первое число: '))
c = int(input('Введите первое число: '))
if c <= a <= b or b <= a <= c:
    print(f'Среднее число: {a = }')
elif a <= b <= c or c <= b <= a:
    print(f'Среднее число: {b = }')
elif a <= c <= b or b <= c <= a:
    print(f'Среднее число: {c = }')
else:
    print('Error')
