from random import randint
rand_list = [randint(1, 100) for i in range(20)]
print(rand_list)
first_min = min(rand_list)
rand_list.remove(first_min)
second_min = min(rand_list)
print(f'Минимальные числа в массиве {first_min} и {second_min}')
