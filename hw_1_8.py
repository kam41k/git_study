year = int(input('Введите год: '))
if year % 4 == 0:
    if year % 100 != 0:
        print(f'Год {year} является високосным.')
    elif year % 100 == 0 and year % 400 == 0:
        print(f'Год {year} является високосным.')
    elif year % 100 == 0 and year % 400 != 0:
        print(f'Год {year} является невисокосным.')
    else:
        print('Error')
elif year % 4 != 0:
    print(f'Год {year} является невисокосным.')
else:
    print('Error')
