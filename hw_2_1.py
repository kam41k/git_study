while True:
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    while True:
        c = input('Введите знак операции, для выхода из программы введите "0": ')
        if c not in ('+', '-', '/', '*', '0'):
            print('Вы ввели неверную операцию.')
            continue
        elif c == '0':
            exit()
        elif c in ('+', '-', '/', '*', '0'):
            break
    if c == '/':
        if b == 0:
            print('На ноль делить нельзя.')
            continue
        elif b != 0:
            print(f'{a / b = }')
    elif c == '+':
        print(f'{a + b = }')
    elif c == '-':
        print(f'{a - b = }')
    elif c == '*':
        print(f'{a * b = }')
