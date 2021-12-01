from random import randint
rand_list = [randint(50, 100) for i in range(100)]
rand_set = list(set(rand_list))
max_cnt = 0
num_max_cnt = 0
for item in rand_set:
    if rand_list.count(item) > max_cnt:
        max_cnt = rand_list.count(item)
        num_max_cnt = item
print(f'Число встречающееся максимально в списке - {num_max_cnt}, встречается {max_cnt} раз.')
