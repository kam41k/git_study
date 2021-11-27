user_num_quan = input('Введите количество чисел для сравнения: ')
num_with_max_sum = 0
max_num_sum = 0
curr_num = 0
curr_num_sum = 0
i = 1
while i <= int(user_num_quan):
    curr_num_sum = 0
    curr_num = input('Введите число натуральное число: ')
    if curr_num.isdigit() and int(curr_num) > 0:
        i += 1
        for _ in curr_num:
            curr_num_sum += int(_)
        if curr_num_sum > max_num_sum:
            max_num_sum = curr_num_sum
            num_with_max_sum = curr_num
    elif not curr_num.isdigit() or int(curr_num) < 1:
        print('Вы ввели неверное число.')
print(f'Число с максимальной суммой цифр - {num_with_max_sum} сумма цифр числа равна - {max_num_sum}.')
