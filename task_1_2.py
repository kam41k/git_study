# функция для вычисления суммы цифр числа
def dig_sum(num):
    digits_sum = num % 10
    pwr = 1
    while num // 10 ** pwr > 0:
        digits_sum += num // 10 ** pwr % 10
        pwr += 1
    return digits_sum

#функция подсчета суммы чисел, сумма цифр которых делится нацело на 7
def cubes_sum_7(cubes_list):
    cubes_sum = 0
    for num in cubes_list:
        if dig_sum(num) % 7 == 0:
            cubes_sum += num
    return cubes_sum


#Задание 2а
cubes_list = [num ** 3 for num in range(1,1000,2)]
print(cubes_sum_7(cubes_list))

#Задание 2b+c
cubes_list = [num + 17 for num in cubes_list[:]]
print(cubes_sum_7(cubes_list))