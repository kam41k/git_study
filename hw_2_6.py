from random import randint
hid_num = randint(1, 100)
print('Попробуйте отгадать, загаданное число от 1 до 100, за 10 попыток.')
for i in range(10):
    user_num = int(input('Введите ваше число от 1 до 100: '))
    if user_num not in range(1, 101):
        print('Вы ввели неверное число.')
    elif user_num in range(1, 101):
        if user_num == hid_num:
            print(f'Абсолютно верно, загаданное число - {hid_num}')
            exit()
        elif user_num > hid_num:
            print('Ваше число больше загаданного.')
        elif user_num < hid_num:
            print('Ваше число меньше загаданного.')
    print(f'У вас осталось {9-i} попыток.')
print(f'К сожалению попытки закончились, загаданное число - {hid_num}')
