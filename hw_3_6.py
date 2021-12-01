from random import randint
rand_list = list(set([randint(1, 100) for i in range(20)]))
print(rand_list)
min_num = min(rand_list)
max_num = max(rand_list)
if rand_list.index(min_num) < rand_list.index(max_num):
    sum_list = rand_list[rand_list.index(min_num)+1:rand_list.index(max_num)]
elif rand_list.index(min_num) > rand_list.index(max_num):
    sum_list = rand_list[rand_list.index(max_num) + 1:rand_list.index(min_num)]
print(sum_list)
print(f'Сумма элементов между минимальным и максимальным элементом - {sum(sum_list)}')
