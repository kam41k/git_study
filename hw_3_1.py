num_list = [i for i in range(2, 100)]
div_list = [i for i in range(2, 10)]
for div in div_list:
    print(f'Количество чисел в списке, делящийхся на {div} - {len([i for i in num_list if i % div == 0])}')
