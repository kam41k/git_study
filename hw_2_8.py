user_num = int(input('Введи цифру, для которой необходимо подсчитать количество повторений в '
                     'заданной последовательности чисел: '))
user_num_cnt = 0
user_row_len = int(input('Введите длину последовательности чисел: '))
user_row_num = 0
for i in range(user_row_len):
    user_row_num = input('Введите число в последовательности: ')
    for _ in user_row_num:
        if user_num == int(_):
            user_num_cnt += 1
print(f'Количество повторений цифры {user_num} в заданной последовательности чисел - {user_num_cnt}')
