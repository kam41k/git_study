from random import randint
rand_list = [randint(1, 1000) for i in range(20)]
print(rand_list)
# "Горячая" перестановка элементов для Python 10
rand_list[rand_list.index(max(rand_list))], rand_list[rand_list.index(min(rand_list))] = \
            rand_list[rand_list.index(min(rand_list))], rand_list[rand_list.index(max(rand_list))]
print(rand_list)
